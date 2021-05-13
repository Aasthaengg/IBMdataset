a,b,c=map(int,input().split())
s = [a,b,c]
s = sorted(s)
print('Yes' if s[0]+s[1]==s[2] else 'No')