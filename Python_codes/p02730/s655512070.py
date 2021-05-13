
s = input()
n = len(s)
cen1 = int((n-1)/2)
cen2 = int((n+3)/2)
if s == s[::-1] and s[:cen1] == s[cen1-1::-1] and s[cen2-1:n] == s[n:cen2-2:-1]:
    print('Yes')
else:
    print('No')
