n = int(input())
s = input()
t = s[n//2:]


if s == t*2:
    print('Yes')
else:
    print('No')