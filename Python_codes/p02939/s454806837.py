s = input()
cnt = 0
i = 1
while i < len(s):
    if s[i] == s[i-1]:
        cnt += 1
        i += 3
    else:
        i += 1
print(len(s)-cnt)