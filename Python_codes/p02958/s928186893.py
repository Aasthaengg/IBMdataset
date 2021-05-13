n = int(input())
A = list(map(int,input().split()))
B = sorted(A)
dif = 0
for i in range(n):
  if A[i]!=B[i]:
    dif+=1
if dif==0 or dif==2:
  print("YES")
else:
  print("NO")