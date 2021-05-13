N = int(input())
As =  list(map(int, input().split()))

for i in range(N):
  As[i] -= i+1
  
As.sort()

rlt = 0
n = N//2
for a in As:
  rlt += abs(a-As[n])

print(rlt)