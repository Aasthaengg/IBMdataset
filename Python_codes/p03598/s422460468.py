n = int(input())
k = int(input())
x = list(map(int,input().split()))
sum = 0
for i in range(n):
  if x[i] <= abs(x[i]-k):
    sum += x[i]*2
  else:
    sum += abs(x[i]-k)*2

print(sum)