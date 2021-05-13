N = int(input())
M = N*(N-1)//2-N//2
print(M)
if N%2 ==0:
  rem = N+1
else:
  rem = N
#print(rem)
for i in range(N):
  i +=1 #1index
  for j in range(i,N):
    j +=1 #1index
    temp = [i,j]
    if i+j != rem:
      print(*temp)