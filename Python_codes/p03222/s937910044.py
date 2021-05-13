H,W,K = map(int,input().split())
MOD = 10**9+7

if W == 1:
  print(1)
  exit()

possible = []
for i in range(1<<(W-1)):
  b = bin(i)[2:]
  flag = 1
  for j in range(len(b)-1):
    if b[j] == b[j+1] == "1":
      flag = 0
  if flag:
    possible.append(int(b,2))

def amida(b):
  ret = [i for i in range(W)]
  for i in range(W-1):
    if b>>i & 1:
      ret[i],ret[i+1] = ret[i+1],ret[i]
  return ret

ans = [0 for i in range(W)]
ans[0] = 1

for _ in range(H):
  new_ans = [0 for i in range(W)]
  for b in possible:
    for i in range(W):
      new_ans[i] = (new_ans[i] + ans[amida(b)[i]])%MOD
  ans = new_ans
  
print(ans[K-1])