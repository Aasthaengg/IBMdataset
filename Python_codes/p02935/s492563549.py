n=int(input())
vv=list(sorted(map(int,input().split())))
now=vv[0]
for i in range(1,n):
  now=(now+vv[i])/2
print(now)
