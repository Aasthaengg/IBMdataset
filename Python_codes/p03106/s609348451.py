a,b,k = map(int,input().split())
ans = []
ab = [a,b]
for i in range(1,max(ab)+1):
  if(a%i == 0 and b%i == 0):
    ans.append(i)
    
print(ans[-k])