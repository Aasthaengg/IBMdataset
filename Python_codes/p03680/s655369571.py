N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

visited = set([])
cur = 0
ok = False

while True:
    if not (cur in visited):
        visited.add(cur)
    else:
        break
    cur = A[cur] - 1
    if cur == 1:
        ok = True
        break
if ok:
    print(len(visited))
else:
    print(-1)