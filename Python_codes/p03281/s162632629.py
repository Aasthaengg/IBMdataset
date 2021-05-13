n=int(input())
#n,m=map(int,input().split())
#hl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

def divnum(n):
    res=0
    for i in range(1,n+1):
        if n%i==0:
            res+=1
    if res==8:
        return True
    else:
        return False
count=0
for i in range(1,n+1):
    if i%2!=0 and divnum(i):
        count+=1
print(count)