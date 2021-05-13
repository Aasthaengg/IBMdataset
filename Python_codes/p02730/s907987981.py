s = input()

n = len(s)
i = int((n-1)/2)
t = s[:i]
ii = int((n+3)/2-1)
u = s[ii:]

if s == s[::-1] and t == t[::-1] and u == u[::-1]:
    print('Yes')
else:
    print('No')