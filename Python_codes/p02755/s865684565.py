A,B = map(int,input().split())
X1 = int(A // 0.08)
X2 = int( (A+1) // 0.08)
array1 = []
for i in range(X1+1,X2):
  array1 += [i]
Y1 = int(B // 0.1)
Y2 = int( (B+1) // 0.1)
array2 =[]
for j in range(Y1+1,Y2):
  array2 += [j]
N1 = len(array1)
for t in range(N1):
  if array1[t] in array2:
    print(array1[t])
    exit()
print(-1)
