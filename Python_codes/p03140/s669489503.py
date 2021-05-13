n=int(input())
arr=[input() for _ in range(3)]
ans=0
for i in range(n):
  if arr[0][i]==arr[1][i] and arr[1][i]==arr[2][i]:
    tmp=0
  elif arr[0][i]==arr[1][i] or arr[1][i]==arr[2][i] or arr[2][i]==arr[0][i]:
    tmp=1
  else:
    tmp=2
  ans+=tmp
print(ans)