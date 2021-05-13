N, M = map(int, input().split())
*H, = map(int, input().split())
d = {i:[] for i in range(1, N+1)}
for _ in range(M):
    A, B = map(int, input().split())
    d[A].append(B)
    d[B].append(A)

ans = 0
for i in range(1, N+1):
    cd = [H[j-1] for j in d[i]]
    v = max(cd) if cd else 0
    if H[i-1]>v:
        ans += 1

print(ans)
