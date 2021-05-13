N=int(input())
d=sorted(list(map(int,input().split())))
l=len(d)
a=d[int(l/2)]
b=d[int(l/2)-1]
x=0
for i in range(b,a):
    x+=1
print(x)