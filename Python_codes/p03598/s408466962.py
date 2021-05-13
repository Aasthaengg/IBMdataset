N = int(input())
K = int(input())
x = [int(i) for i in input().split()]

suml = [0] * N

for i in range(N):
  delta = abs(K-x[i])
  if x[i] < delta:
  	suml[i] = suml[i] + x[i]*2
  else:
  	suml[i] = suml[i] + delta*2

print(sum(suml))