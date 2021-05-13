N=int(input())
a=[int(input()) for _ in range(N)]

btn=1
cnt=0

while True:
  btn=a[btn-1]
  cnt+=1
  if btn==2:
    print(cnt)
    break
  if cnt>N:
    print(-1)
    break