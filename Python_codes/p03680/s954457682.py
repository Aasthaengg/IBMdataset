n=int(input())
l=[0]+[int(input())for i in range(n)]
now=1
for i in range(n+5):
    now=l[now]
    if now==2:print(i+1);break
else:print(-1)