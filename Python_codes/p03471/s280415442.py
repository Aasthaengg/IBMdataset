n,y=map(int,input().split())
a,b,c=-1,-1,-1
for i in range(n+1):
    for j in range(n+1-i):
        if 10000*i+5000*j+1000*(n-i-j)==y:
            a=i
            b=j
            c=n-i-j

print(a,b,c)