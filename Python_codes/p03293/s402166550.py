s = list(input())
t = list(input())
for i in range(len(s)):
    if s == t:
        print('Yes')
        exit(0)
    a = s[0]
    s.pop(0)
    s.append(a)
print('No')