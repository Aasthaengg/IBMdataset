n=int(input())
a=list(map(int,input().split()))
cnt=0
i=0
s=sum(a)
while cnt<s//2:
    temp=cnt
    cnt+=a[i]
    i+=1
    
print(min(abs(sum(a)-temp*2),abs(sum(a)-cnt*2)))