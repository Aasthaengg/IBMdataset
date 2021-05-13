a,b,k = list(map(int, input().split()))
ans=[b-i for i in range(k) if b-i>=a]
ans.extend([a+i for i in range(k) if a+k<=b])
ans.sort()
ans=set(ans)
for item in ans:
  print(item)