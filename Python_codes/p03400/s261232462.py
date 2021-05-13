def choco(d,ai):
    day = 1
    ans = 0
    while day<=d:
        ans += 1
        day += ai
    return ans

n = int(input())
d,x = map(int,input().split())
ans = 0
for i in range(n):
    a = int(input())
    ans += choco(d,a)
print(ans + x)