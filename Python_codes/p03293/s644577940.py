s = input()
t = input()
ans = False
for i in range(len(s)):
    if s == t:
        ans = True
    else:
        t = t[1:] + t[0]
print("Yes" if ans else "No")

