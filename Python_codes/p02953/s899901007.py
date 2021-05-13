n = int(input())
h = list(map(int, input().split()))
h = h[::-1]
ans = ''
for i in range(1, n):
  if h[i - 1] >= h[i]:
    next
  elif h[i] - h[i - 1] == 1:
    h[i] = h[i] - 1
  else:
    ans = 'No'
    break
if ans == '':
  ans = 'Yes'
print(ans)