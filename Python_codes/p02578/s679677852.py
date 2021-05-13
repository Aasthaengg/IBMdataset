
n=int(input())
l=list(map(int,input().split()))

x = 0
for a in range(n-1):
    if l[a]>l[a+1] :
        x=l[a] - l[a+1] + x
        l[a+1]=l[a]
    #print("l[a],x,l[a+1]=", l[a], x, l[a+1])
print(x)
