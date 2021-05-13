N=int(input())
List = list(map(int, input().split()))

ans=0
i=0
while i<N:
    
    ans+=(1/List[i])
    
    i+=1

print(1/ans)