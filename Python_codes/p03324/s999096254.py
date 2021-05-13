d, n = (int(i) for i in input().split())
ans = 100**d
add = ans
for i in range(n-1):
    ans += add
    if ans / (100**d) % 100 == 0:
        ans += add
print(ans)
