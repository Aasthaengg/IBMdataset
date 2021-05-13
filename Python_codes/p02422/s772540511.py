class Reader:
    def __init__(self, s):
        self.t = list(s)

    def __call__(self, s):
        t = s.split()
        l, r = int(t[1]), int(t[2])+1
        if t[0] == "reverse":
            for i, v in zip(range(l,r), reversed(self.t[l:r])):
                self.t[i] = v
        elif t[0] == "replace":
            for i, v in zip(range(l,r), t[3]):
                self.t[i] = v
        else:
            print("".join(self.t[l:r]))

reader = Reader(input())
n = int(input())
for _ in range(n):
    reader(input())