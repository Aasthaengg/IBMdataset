n = int(input())
a = list(map(int,input().split()))
t = a[0]
ans = 0
for i in a:
    ans += max(0,t-i)
    t = max(t,i)
print(ans)