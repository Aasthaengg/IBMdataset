s=input()
now = s[0]
res = 0
for char in s:
    if now != char:
        res += 1
    now = char
print(res)

