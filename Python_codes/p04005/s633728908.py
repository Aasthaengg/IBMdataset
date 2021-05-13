A,B,C = map(int,input().split())

if((A%2 == 0)or(B%2 == 0)or(C%2 == 0)):
  ans = 0
else:
  max_num = max(A,B,C) 
  if(max_num == A): 
    ans = 1*B*C
  elif(max_num == B):
    ans = 1*A*C
  else:
    ans = 1*A*B

print(ans)    