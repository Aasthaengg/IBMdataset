s=0
A,B=map(int,input().split())
if A>=B:
  s+=A
  A=A-1
else:
  s+=B
  B=B-1
if A>=B:
  s+=A
  A=A-1
else:
  s+=B
  B=B-1
print(s)