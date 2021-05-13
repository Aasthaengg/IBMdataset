n = int(input())

ans = ""
while n != 0:
    rest = n % 2
    if rest == 1:
        ans += "1"
    else:
        ans += "0"

    n = (n - rest) // -2

if ans == "":
    ans += "0"

print(ans[::-1])

