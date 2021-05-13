N, K = map(int, input().split())
V = list(map(int, input().split()))
R = min(N, K)
ans = 0
for a in range(R+1):
  for b in range(R+1-a): #操作Aをa回、操作Bをb回
    tmp = list()
    for i in range(a): 
      tmp.append(V[i])
    for j in range(b):
      tmp.append(V[N-1-j])
    tmp.sort()
    x = min(K-a-b, len(tmp))
    for k in range(x):
      if(tmp[k] < 0):
        tmp[k] = 0
    ans = max(ans, sum(tmp))
print(ans)