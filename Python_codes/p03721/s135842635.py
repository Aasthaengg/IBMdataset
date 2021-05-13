N,M = map(int,input().split())
dic = {}
for _ in range(N):
  a, b = map(int,input().split())
  if a in dic:
    dic[a] += b
  else:
    dic[a] = b
List = sorted(dic)
ans = 0
i = 0
while M > 0:
  M -= dic[List[i]]
  ans = List[i]
  i += 1
print(ans)