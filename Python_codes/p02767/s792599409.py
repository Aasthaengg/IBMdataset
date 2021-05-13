N = int(input())
ans = 10**8
array = list(map(int,input().split()))
for i in range(0,101):
  energy = 0
  for t in array:
    energy += ( t - i ) ** 2
  ans = min(ans,energy)
print(ans)
    
