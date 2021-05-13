n = int(input())
d = sorted(list(map(int,input().split())))
m = int(input())
t = sorted(list(map(int,input().split())))
ans = 'YES'
x = 0
for i in t:
    while  x<n and d[x]<i:
        x+=1
    if x==n or i!=d[x]:ans='NO'
    else:x+=1
print(ans)