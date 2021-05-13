N, M = map(int, input().split())
r = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    r[a-1] += 1
    r[b-1] += 1

for i in range(N-1):
    if r[i]%2==1:
        print("NO")
        break
else:
    print("YES")