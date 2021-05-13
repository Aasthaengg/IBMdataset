from collections import deque

n = int(input())
abl = []
suml = []
for _ in range(n):
    a,b = map(int, input().split())
    abl.append((a,b))
    suml.append((a+b,a,b))

suml.sort(reverse=True)
q = deque(suml)

asum = 0
bsum = 0
a_turn = True
while q:
    if a_turn:
        _, poped, _ = q.popleft()
        asum += poped
    else:
        _, _, poped = q.popleft()
        bsum += poped
    a_turn = not a_turn

print(asum-bsum)