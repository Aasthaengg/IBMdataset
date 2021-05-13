N = int(input())
a = list(map(int,input().split()))
ans = 0
flag = 0
for i in range(1,N):
  if a[i - 1] == a[i] and flag == 0: 
    ans += 1
    flag = 1
  else: flag = 0  
print(ans)   