s = str(input())
temp = s[0]
X = []
cnt = 0
for i in range(len(s)):
    if s[i] == temp:
        cnt += 1
    else:
        temp = s[i]
        X.append(cnt)
        cnt = 1
else:
    X.append(cnt)
print(len(X)-1)
