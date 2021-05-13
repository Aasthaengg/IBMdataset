x = input()
y = input()
s = x + y
count = 0
ans = ""
for i in range(len(s)):
    if count%2 == 0:
        ans += s[count//2]
        count += 1
    else:
        ans += s[count//2+len(x)]
        count+=1
print(ans)