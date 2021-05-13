N = int(input())
As = list(map(int, input().split()))

As.sort(reverse=True)

rlt = 0

for i in range(N):
  rlt += As[2*i+1]
  
print(rlt)