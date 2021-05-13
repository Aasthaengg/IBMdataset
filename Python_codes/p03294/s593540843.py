n = int(input())
lst = list(map(int,input().split()))
nums = 1
for i in range(n):
  nums *=lst[i]
           
ans = 0
for i in range(n):
  ans += (nums-1)%lst[i]
  
print(ans)