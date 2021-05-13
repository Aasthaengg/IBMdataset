
N, K = list(map(int, input().split()))
point= list(map(int, input().split()))
T = list(input())
d = dict()
d['s'] = point[0]
d['p'] = point[1]
d['r'] = point[2]
res = 0
ans = []
flag = [0,0,0]

for i in range(K):
  res += d[T[i]]
  ans.append(T[i])
for i in range(K,N):
  if ans[i-K] == T[i]:
    ans.append("n")
  else:
    res += d[T[i]]
    ans.append(T[i])
print(res)