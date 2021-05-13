from collections import Counter


N = int(input())
ans = 0
for i in range(1, N+1):
    c = N//i
    ans += i*c*(c+1)//2

print(ans)
