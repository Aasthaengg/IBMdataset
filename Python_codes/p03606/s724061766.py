N = int(input())
ans = 0
for i in range(0, N):
    l, r = (int(j) for j in input().split())
    ans += r-l+1
print(ans)