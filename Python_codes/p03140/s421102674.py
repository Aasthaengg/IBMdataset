N=int(input())
A=list(input())
B=list(input())
C=list(input())

answer=0
for i in range(N):
  a=A[i]
  b=B[i]
  c=C[i]
  
  if a==b==c:
    continue
  elif a==b or b==c or c==a:
    answer+=1
  else:
    answer+=2
    
print(answer)