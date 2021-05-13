a,b,c=map(str,input().split())
o=a[-1:];p=b[0];q=b[-1:];r=c[0]
if o == p and q == r:
  print('YES')
else:
  print('NO')