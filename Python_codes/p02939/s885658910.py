s = input()
ans = 0
a = b = ""
for i in s:
    b += i
    if a != b:
        a = b
        b = ""
        ans += 1
print(ans)
