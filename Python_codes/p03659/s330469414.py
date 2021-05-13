N = int(input())
A = list(map(int,input().split()))
cums = [0]
for a in A:
    cums.append(cums[-1] + a)

ans = 10**20
for i in range(1,N):
    x = cums[i]
    y = cums[-1] - cums[i]
    ans = min(ans, abs(x-y))
print(ans)