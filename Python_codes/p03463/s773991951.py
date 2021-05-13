N,A,B = map(int,input().split())

#print(A,B)

for i in range(N):
  if A+1<B:
    A +=1
  else:
    A += -1
    if A <1:
      ans="Borys"
      break
  #print(i,A,B)
    
  if A<B-1:
    B += -1
  else:
    B += 1
    if B >N:
      ans="Alice"
      break
  #print(i,A,B)
else:
  ans="Draw"
  
print(ans)