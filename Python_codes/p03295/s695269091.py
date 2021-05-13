# D - Islands War

N, M = map(int, input().split())
Q = []
for _ in range(M):
    a, b = map(int, input().split())
    Q.append((a, b))
Q.sort(key = lambda x: x[1])

ans = []
for i in range(M):
    (a, b) = Q[i]
    if ans == [] or ans[-1] < a:
        ans.append(b-1)
    else:
        continue
print(len(ans))