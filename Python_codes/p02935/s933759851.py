# C - Alchemist
N = int(input())
v = list(map(int,input().split()))
v.sort(reverse=True)
ans = 0
for i in range(N):
    ans += v[i]/(2**(i+1))
ans += v[-1]/(2**N)
print(ans)