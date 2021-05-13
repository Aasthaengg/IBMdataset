ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n,x = nm()
m=[]

for i in range(n):
  mm = ni()
  m.append(mm)

m = sorted(m)

cnt=n
x-=sum(m)

for i in range(n):
  while x>0:
    if x>=m[i]:
      x-=m[i]
      cnt+=1
    else:
      break

print(cnt)