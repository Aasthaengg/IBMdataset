
N = int(input())

ans = ""
x = N
while x > 0:
    cur = (x - 1) % 26
    ans += chr(ord("a") + cur)
    x = (x - 1) // 26

print(ans[::-1])
