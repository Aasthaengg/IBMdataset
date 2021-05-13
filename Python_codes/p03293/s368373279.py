s = str(input())
t = str(input())
count = 0
for i in range(len(s)):
    t = t[-(i + 1)] + t
    if s in t:
        count = 1
    else:
        pass
print("Yes" if count == 1 else "No")