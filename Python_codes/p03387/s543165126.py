a = list(map(int, input().split()))
t = sum(a)
ans = 0
while t%3 > 0 or t < max(a)*3:
    ans, t = ans+1, t+2

print(ans)