n=int(input())
p=list(map(int,input().split()))
x=sorted(p)
d=0
for i in range(n):
    if p[i]!=x[i]:
        d+=1
if d==0 or d==2:
    print("YES")
else:
    print("NO")