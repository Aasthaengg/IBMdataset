s = list(input())
t = list(input())

for i in range(len(s)):
    p = s.pop()
    s.insert(0, p)
    if s == t:
        print('Yes')
        exit()
print('No')