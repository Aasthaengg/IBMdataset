A=int(input())
B=[1]*8
for i in range(2,10):
  for j in range(A+1):
    if j**i <= A:
      B[i-2]= j**i
    else:break
print(max(B))