h = int(input())
ans = 0
num = 1
while h >= 1:
    h //= 2
    ans += num
    num *= 2
print(ans)