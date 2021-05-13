N,K=map(int,input().split())

# 最大公約数が1〜Kになるそれぞれの個数を求める
# 大きい方から順に計算して、自分の倍数になるものは除外する

res = [0] * (K+1)
DIV = 10 ** 9 + 7
for x in range(K,0,-1):
  # 最大公約数がxになるものは
  # K//x個ある
  # (K//x)**Nが、個数
  res[x] = pow(K//x,N,DIV)
  for i in range(x*2,K+1,x):
    res[x] -= res[i]
    
ans = 0
for i in range(len(res)):
  ans += res[i] * i
  ans %= DIV
  
print(ans)