s = input()
flag = False
for i in range(len(s)):
    if not flag:
        if s[i] == 'A':
            p = i
            flag = True
    if flag:
        if s[i] == 'Z':
            q = i
print(q-p+1)