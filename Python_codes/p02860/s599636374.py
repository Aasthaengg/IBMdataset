n = int(input())
s = str(input())
ans = s[0:n//2]
if s == (ans+ans):
    print('Yes')
else:
    print('No')
