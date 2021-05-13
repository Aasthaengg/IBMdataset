N=int(input())
List=list(map(int, input().split()))
ans=0
for i in range(0,N-2):
    if min(List[i],List[i+2])<List[i+1] and max(List[i],List[i+2])>List[i+1]:
        ans+=1
print(ans)