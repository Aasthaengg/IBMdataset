n=int(input())
lists=list(map(int,input().split()))
maxi=0
gives=0
index=0

for i in range(n):
    if abs(lists[i])>maxi:
        maxi=abs(lists[i])
        gives=lists[i]
        index=i
if gives<0:
    print(2*n-2)
    for i in range(n):
        if i!=index:
            print(index+1,i+1)
    for i in range(n-1):
        print(n-i,n-1-i)
elif gives>=0:
    print(2*n-2)
    for i in range(n):
        if i!=index:
            print(index+1,i+1)
    for i in range(n-1):
        print(i+1,i+2)