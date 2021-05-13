n = int(input())
s = input()

ans = ""
for i in s:
    t = ord(i)
    t += n
    if t > 90:
        t -= 26
    ans += chr(t)

print(ans)
