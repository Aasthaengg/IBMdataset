s=input()
n=len(s)
x=n//2
a=s[0:x]
b=s[x+1:]
if a==b:print('Yes')
else:print('No')
