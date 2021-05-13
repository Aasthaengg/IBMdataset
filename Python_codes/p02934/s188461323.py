N=int(input())
List = list(map(int, input().split()))
k = 0
res = 0
for i in range(N):
  k += 1/ List[i]
  res = 1/k
print(res)