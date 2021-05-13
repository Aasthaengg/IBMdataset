import sys
n=int(input())
a=list(map(int,input().split()))
b=1
c=0
for i in range(n):
    if a[i]==b:
        b+=1
    else:
        c+=1
if b==1:
    print(-1)
    sys.exit()
print(c)