s = list(input())
t = list(input())

for i in range(len(s)):
    if s == t:
        print('Yes')
        exit(0)
    a = s[-1]
    s.pop(-1)
    s[0:0] = a

print('No')