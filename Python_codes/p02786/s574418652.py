h = int(input())
ans = 0
t = 1
while h > 0:
    h //= 2
    ans += t
    t *= 2
print(ans)
