import statistics

n=int(input())
l=list(map(int,input().split()))
ans=0
for i in range(n-2):

    l2=[l[i],l[i+1],l[i+2]]
    if statistics.median(l2)==l[i+1]:
        ans+=1

print(ans)