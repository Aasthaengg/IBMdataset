A,B=list(map(int,input().split()))
ct=0
for i in range(A,B+1):
  t=str(i)
  for j in range(len(t)):
    if t[j]!=t[-j-1]:
      break
  else:
      ct+=1
print(ct)