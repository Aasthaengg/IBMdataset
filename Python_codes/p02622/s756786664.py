s = [i for i in input()]
t = [i for i in input()]
c = 0
for i in range(len(s)):
    if s[i] != t[i]:
        c+=1
print(c)