n=int(input())
d,x=map(int,input().split())
ans=0
day=1

for i in range(n):
    a=int(input())
    while True:
        if day>d:
            break
        ans+=1
        day+=a
    day=1
print(ans+x)