N = int(input())
As = list(map(int, input().split()))

As.sort()

Ss = [As[0]]

for i in range(1,N):
  Ss.append(Ss[-1] + As[i])
  
cnt = 0
for i in range(N-1):
  if 2*Ss[i] < As[i+1]:
    cnt = i+1
    
print(N-cnt)