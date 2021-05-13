h,w=map(int,input().split())
n = int(input())
a = list(map(int, input().split()))
data = []
for i in range(1,n+1):
    for j in range(a[i-1]):
        data.append(str(i))

ans = []
for i in range(h):ans.append([])

count = 0
for i in range(h):
    for j in range(w):
        ans[i].append(data[count])
        count+=1

count = 0

for i in ans:
  if(count%2==0):print(' '.join(i))
  else:print(' '.join(list(reversed(i))))
  count+=1