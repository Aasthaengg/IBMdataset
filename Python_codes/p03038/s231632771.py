N, M = map(int,input().split())

A = list(map(int,input().split()))
D = dict()

for a in A:
    if a in D:
        D[a] += 1
    else:
        D[a] = 1

for _ in range(M):
    B, C = map(int,input().split())
    if C in D:
        D[C] += B
    else:
        D[C] = B

D = sorted(D.items(), reverse = True)

ans, cnt = 0, 0
for d in D:
    x = min(d[1], N-cnt)
    cnt += x
    ans += d[0] * x

    if cnt == N: break


print(ans)
