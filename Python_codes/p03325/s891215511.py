n=int(input())
#a,b=map(int,input().split())
al=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
count=0
for a in al:
    temp=0
    v=a
    while v%2==0:
        v=v//2
        temp+=1
    count+=temp

print(count)

