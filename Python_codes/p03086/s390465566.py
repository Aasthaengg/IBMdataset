s = input()
x = list()
cnt = 0
for i in range(len(s)):
    if s[i] == "A" or s[i] == "T" or s[i] == "G" or s[i] == "C":
        cnt += 1
        if i == len(s) - 1:
            x.append(cnt)
    else:
        x.append(cnt)
        cnt = 0
print(max(x))