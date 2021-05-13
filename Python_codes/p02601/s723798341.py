a,b,c = map(int,input().split())
k = int(input())

ans = 'No'
for i in range(k+1):
  if a < b*(2**i) < c*(2**(k-i)):
    ans = 'Yes'
    
print(ans)    
