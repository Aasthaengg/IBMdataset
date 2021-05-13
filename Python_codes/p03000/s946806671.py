n,x = map(int,input().split())
l = list(map(int,input().split()))
sum = 0
ans = 0
for i in l:
  sum += i
  if sum <= x:
    ans += 1
print(ans+1)