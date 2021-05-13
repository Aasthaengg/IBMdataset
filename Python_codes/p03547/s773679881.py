A,B = map(str,input().split())
dic = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6}
An = dic[A]
Bn = dic[B]
if An == Bn:
  print('=')
if An < Bn:
  print('<')
if An > Bn:
  print('>')