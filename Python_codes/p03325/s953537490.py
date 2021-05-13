N = int(input())
a = list(map(int, input().split()))
cnt=0
for i in range(N):
  v = a[i]
  while 1:
    if v%2==0:
      v=v//2
      cnt+=1
    else:
      break

print(cnt)