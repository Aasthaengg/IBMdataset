n=int(input())
a=[int(input()) for i in range(n)]
num=1
res=False
time=1
for j in range(n-1):
    if a[num-1]==2:
        res=True
        time+=j
        break
    else:
        num=a[num-1]

if res:
    print(time)
else:
    print(-1)
