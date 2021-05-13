s = input()
cnt = 0
for i in range(len(s)):
    if s[i] == "o":
        cnt += 1
if cnt+ 15 - len(s) >= 8:
    print("YES")
else:
    print("NO")