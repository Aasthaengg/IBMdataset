import bisect
N = int(input())
List = list(map(int,input().split()))
List.sort()
ans = 0
for i in range(N-1):
  for j in range(i+1, N):
    ans += bisect.bisect_left(List,List[i]+List[j])-(j+1)
print(ans)