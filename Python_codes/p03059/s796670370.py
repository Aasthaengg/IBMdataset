a,b,t = map(int,input().split())
sum = 0

for i in range(1,90):
  if i*a > t+ (1/2):
    ans = i-1
    break
    
for j in range(1,ans+1):
  sum += b
  
  
print(sum)