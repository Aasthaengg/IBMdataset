n=int(input())
d=list(map(int,input().split()))
x=0
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        else:
            x+=d[i]*d[j]
            
print(x//2)