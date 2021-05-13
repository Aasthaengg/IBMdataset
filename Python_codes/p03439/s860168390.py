class Sender:

    def __init__(self):
        self.queue = {}
        self.dict = {
            "Vacant": 0,
            "Male": 1,
            "Female": 2
        }

    def send(self, x) -> bool:
        print(x, flush=True)
        self.queue[x] = self.dict[input()]
        return self.queue[x] == 0

    def compare(self, x, y) -> bool:
        return self.queue[x] == self.queue[y]


n = int(input())
s = Sender()

if s.send(0):
    exit()
if s.send(n - 1):
    exit()
l, r = 0, n-1
m = (n - 1) // 2
q = 2

while not s.send(m):
    q += 1
    if q == 20:
        break
    if ((r - m) % 2 == 0 and not s.compare(r, m)) or ((r - m) % 2 == 1 and s.compare(r, m)):
        l, r = m, r
        m = (r + m) // 2

    else:
        l, r = l, m
        m = (m + l) // 2
