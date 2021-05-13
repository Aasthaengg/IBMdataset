N=int(input())
p=list(map(int,input().split()))

i=0
op=0
while i<N:
    if i+1==p[i]:
        cnt=0
        j=i
        while j<N and p[j]==j+1:
            cnt+=1
            j+=1
        
        op+=(cnt+1)//2
        i=j
    else:
        i+=1

print(op)