t = int(input())
m = list(map(int,input().split()))
x = int(input())
s=sum(m)
for i in range(x):
    e=s
    p,y= (map(int,input().split()))
    e=e-m[p-1]+y
    print(e)
