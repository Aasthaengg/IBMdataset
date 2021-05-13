n=int(input())
d,x=map(int,input().split())
al=[int(input()) for i in range(n)]
total=0
for i in range(n):
    total+=1
    day=al[i]
    while True:
        if day+1<=d:
            total+=1
            day+=al[i]
        else:
            break
print(total+x)

