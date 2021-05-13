n = int(input())
a = list(map(int,input().split()))
max_num = 0
count = 0
for i in range(1,n):
  if a[i-1]>=a[i]:
    count+=1
  else:
    max_num = max(count,max_num)
    count = 0
  if i == n-1:
    max_num = max(count,max_num)
print(max_num)