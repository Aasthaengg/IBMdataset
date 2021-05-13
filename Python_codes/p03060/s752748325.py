n = int(input())
v = list(map(int,input().split()))
c = list(map(int,input().split()))
l = [v[i]/c[i] for i in range(n)]
x,y=0,0
for k,i in enumerate(l):
    if i>=1:
        x+=v[k]
        y+=c[k]
print(x-y)