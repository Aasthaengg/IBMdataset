a, b, x = map(int, input().split(" "))

ad = a // x
bd = b // x
ans = bd - ad
if a % x == 0:
    ans += 1
print(ans)