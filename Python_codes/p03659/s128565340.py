N = int(input())
A = list(map(int,input().split()))
cums = [0]
for a in A:
    cums.append(cums[-1] + a)
ans = float('inf')
for i in range(1,N):
    c = cums[i]
    ans = min(ans, abs(cums[-1]-c - c))
print(ans)