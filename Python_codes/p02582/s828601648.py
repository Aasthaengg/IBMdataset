# A
s = input()
count = 0
ans = 0
for i in range(len(s)):
    if s[i] == "R":
        count += 1
    else:
        if ans < count:
            ans = count
        count = 0
if ans < count:
    ans = count
print(ans)
