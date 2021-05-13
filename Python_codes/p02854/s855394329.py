n = int(input())
s = list(map(int,input().split()))
ans = 2020202020
a = 0
b = sum(s)
for i in range(n):
    a += s[i]
    b -= s[i]
    ans = min(ans,abs(a-b))
print(ans)