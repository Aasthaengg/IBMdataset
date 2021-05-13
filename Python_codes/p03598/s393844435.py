N = int(input())
K = int(input())
List = list(map(int, input().split()))
res = 0
for i in range(N):
  res += min(K-List[i],List[i])
res = 2 * res
print(res)