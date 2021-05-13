n=int(input())
a=list(map(int,input().split()))
arr=[0]*(10**5+1)
for i in a:
    arr[i]+=1


s=sum(a)

for i in range(int(input())):
    b,c=map(int,input().split())
    arr[c]+=arr[b]
    s=s+arr[b]*c-arr[b]*b
    arr[b]=0
    print(s)
