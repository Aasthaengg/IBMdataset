import heapq

N, K = map(int, input().split())
heap = []
types = [0 for _ in range(N)]

class Sushi():
    def __init__(self, neta, aji):
        self.neta = neta - 1
        self.aji = aji

    def __str__(self):
        return "Sushi{0}: {1}".format(self.neta, self.aji)

    def reverse(self):
        self.aji = -self.aji

    def __lt__(self, other):
        return self.aji < other.aji

for _ in range(N):
    t, d = map(int, input().split())
    heap.append(Sushi(t, -d))
heapq.heapify(heap)

variety = 0
basic = 0
choices = []
for _ in range(K):
    sushi = heapq.heappop(heap)
    sushi.reverse()
    basic += sushi.aji
    neta = sushi.neta
    if types[neta] == 0:
        variety += 1
    types[neta] += 1
    choices.append(sushi)
heapq.heapify(choices)

satisfaction = basic + variety * variety
top_satisfaction = satisfaction
while True:
    drop_sushi = None
    while len(choices) > 0:
        choiced_sushi = heapq.heappop(choices)
        if types[choiced_sushi.neta] > 1:
            drop_sushi = choiced_sushi
            types[choiced_sushi.neta] -= 1
            break
    add_sushi = None
    while len(heap) > 0:
        new_sushi = heapq.heappop(heap)
        new_sushi.reverse()
        if types[new_sushi.neta] == 0:
            types[new_sushi.neta] += 1
            add_sushi = new_sushi
            break
    if drop_sushi is None or add_sushi is None:
        break
    else:
        variety += 1
        basic += add_sushi.aji - drop_sushi.aji
        satisfaction = basic + variety * variety
        if satisfaction > top_satisfaction:
            top_satisfaction = satisfaction
print(top_satisfaction)
