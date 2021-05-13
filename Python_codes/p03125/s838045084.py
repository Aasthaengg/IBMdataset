A, B=map(int,input().split())
 
N = B % A
 
if N==0:
  Ans = A+B
else:
  Ans = B-A

print(Ans)