n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
x,y=0,0
for i in range(n):
    if(i%2==0):
        x+=l[i]
    else:
        y+=l[i]
print(abs(x-y))