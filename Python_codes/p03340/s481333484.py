N = int(input())
A = list(map(int,input().split()))


xor = [0]*(N+1)
cum = [0]*(N+1)
for i in range(N):
    xor[i] = xor[i-1]^A[i]
    cum[i] = cum[i-1]+A[i]

rlist = []
r = 0
for l in range(N):
    r = max(l+1,r)
    while r < N and xor[r]^xor[l-1] == cum[r]-cum[l-1]:
        r += 1
    if r == N:
        break
    r -= 1
    rlist.append(r)
ans = 0
rlist += [N-1]*(N-len(rlist))
for l in range(N):
    r = rlist[l]
    ans += r-l+1
print(ans)