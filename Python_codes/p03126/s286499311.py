N, M = map(int,input().split())
dish = [0 for i in range(M)]
for i in range(N):
  like = list(map(int,input().split()))
  for i in like[1:]:
    dish[i-1]+=1
ans = dish.count(N)
print(ans)