s = list(input())
t = list(input())

if len(s)+1 == len(t):
    for i in range(len(s)):
        if s[i] != t[i]:
            print('No')
            break
        elif i == len(s)-1:
            print('Yes')
else:
    print('No')
