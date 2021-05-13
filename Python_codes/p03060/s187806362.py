n = int(input())
v = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

arr = [x-y for x,y in zip(v,c)]

ans = 0
for i in arr:
  if i > 0:ans+=i
    
print(ans)



