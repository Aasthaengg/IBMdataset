n = int(input())
ans = []

if n == 0:
    print(0)
    exit()
while n != 0:
    if n%2 == 1:
        ans += "1"
        n -= 1
    else:
        ans += "0"
    n //= -2
print("".join(ans[::-1]))