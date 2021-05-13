n = int(input())
s = input()

ans = ''
for c in s:
    o = ord(c)
    if o+n > 90:
        ans += chr(o+n-26)
    else:
        ans += chr(o+n)

print(ans)