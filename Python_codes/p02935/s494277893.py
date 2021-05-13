n=int(input())
List=list(map(int,input().split()))
List.sort()
ans=(List[0]+List[1])/2
for i in range(n-2):
    ans=(ans+List[i+2])/2
print(ans)