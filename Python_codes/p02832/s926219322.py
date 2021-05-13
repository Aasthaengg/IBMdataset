x=int(input())
s=list(map(int,input().split()))
p=0
c=1
for n in s:
    if n==c:
        c+=1
        p+=1

if p==0:
    print(-1)
    exit(0)
print(x-p)