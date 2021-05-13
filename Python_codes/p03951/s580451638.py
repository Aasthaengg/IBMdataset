n= int(input())
s= input()
t= input()
if s==t: print(len(s)); exit()
for i in range(1,n+1):
  a=s+t[-i:]
  b=s[:i]+t
  if a==b: print(len(a)); break
