A,B,C=map(int,input().split())
if A+B+1>=C:
    n=C
else:
  n=A+B+1
n+=B
print(n)