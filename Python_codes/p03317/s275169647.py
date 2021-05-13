n,k=map(int,input().split())
a=list(map(int,input().split()))
count=1
n=n-k
while(n>0):
    n=n-(k-1)
    count+=1
print(count)