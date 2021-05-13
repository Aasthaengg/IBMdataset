n=int(input())
l=[list(map(int, input().split())) for i in range(n)]
for i in range(n-1):
    a=1
    b=1
    if l[i+1][0]<l[i][0]:
        a=-(-l[i][0]//l[i+1][0])
    if l[i+1][1]<l[i][1]:
        b=-(-l[i][1]//l[i+1][1])
    l[i+1][0]*=max(a,b)
    l[i+1][1]*=max(a,b)
print(sum(l[-1]))