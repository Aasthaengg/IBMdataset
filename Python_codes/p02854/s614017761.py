n = int(input())
a = list(map(int,input().split()))
r = ans = sum(a)
l = 0
ans = float('inf')
for i in a:
    r -= i
    l += i
    ans = min(ans,abs(r-l))
print(ans)