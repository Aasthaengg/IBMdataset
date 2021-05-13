N = int(input())

A = [2,1]

for i in range(2,90):
  temp = A[i-1]+A[i-2]
  A.append(temp)
ans = A[N]
print(ans)