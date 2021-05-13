n=int(input())
p=list(map(int,input().split()))
m=10000000
count=0
for i in range(n):
    if p[i]==min(p[i],m):
        count+=1
    m=min(p[i],m)
print(count)