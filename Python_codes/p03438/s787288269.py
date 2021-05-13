N = int(input())
a= list(map(int,input().split()))
b= list(map(int,input().split()))
c = [a[i]-b[i] for i in range(N)]
d=sum(b)-sum(a)   #c回試行する
if d<0:
  print("No")
  exit()
  
must=0
cnt=0
for num in c:
  if num>0:
    must += abs(num)
  if num*(-1) >= 2:
    cnt += (-1)*num//2
if must>d:
  print("No")
  exit()

#nokori = d-must
#print(must,nokori,cnt)

if cnt<must:
  print("No")
else:
  print("Yes")
