n = int(input())
ans = ""
if n == 0:
    print(0)
    exit()
while n != 0:
    if n%(-2) == -1:
        ans += "1"
    else:
        ans += "0"
    n //= 2
    n *= -1
print(ans[::-1])