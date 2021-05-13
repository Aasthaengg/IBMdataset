N=int(input())
List = list(map(int, input().split()))
res = List[0]
for i in range(N-2):
  res += min(List[i],List[i+1])
res+=List[N-2]
print(res)