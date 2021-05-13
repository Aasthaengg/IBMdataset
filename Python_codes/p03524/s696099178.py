s = str(input())
A = [0,0,0]
for a in s:
  if a=='a':A[0]+=1
  if a=='b':A[1]+=1
  if a=='c':A[2]+=1

if max(A)-min(A)>=2:
  print("NO")
else:
  print("YES")
