n = int(input())
a = list(map(int, input().split()))
t = sum(a)
ans = sum(a)
l = 0
for i in a:
    l += i 
    r = t-l
    ans = min(ans, abs(l-r))
print(ans)