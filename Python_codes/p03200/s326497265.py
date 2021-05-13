s = input()
l = len (s)
se = set()
for i in range(l):
    if s[i]=='W':
        se.add(i)
n = len(se)

ans = sum(se) - n*(n-1)//2
print(ans)
