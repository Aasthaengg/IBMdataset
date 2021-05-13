s = input()
n = len(s)
sl = s[:n//2]
sr = s[n//2+1:]
if sl == sr and sr ==  sr[::-1]:
    print('Yes')
else:
    print('No')