n = int(input())
h = list(map(int,input().split()))
ans = 'Yes'
temp = h[0]
for i in range(1,n):
  if h[i]>temp:
    h[i] -= 1
  elif temp>h[i]:
    ans = 'No'
  temp = h[i]
print(ans)