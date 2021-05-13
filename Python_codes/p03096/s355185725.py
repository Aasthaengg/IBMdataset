N=int(input())
MOD=10**9+7
memo={}

#prev_numがその時点での組み合わせ数
prev_num=1
prev=None

for _ in range(N):
  c=int(input())
  if c==prev:
    continue
  tmp=prev_num
  if c in memo:
    tmp+=memo[c]
  tmp%=MOD
  #memo[c]にそれまでの組み合わせの数が入ることで、
  #次にcが出てきた時にどれぐらい通りが増えるかが分かる
  memo[c]=tmp
  prev_num=tmp
  prev=c
print(prev_num)