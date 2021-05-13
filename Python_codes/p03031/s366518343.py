import sys
N,M =map(int, input().split())
q = list()

for i in range(M):
  q.append(list(map(int, input().split()))) #q[0]はqのlength
p = list(map(int, input().split())) #スイッチの偶奇正解を示す

ans = 0

for s in range(2**N):  #sは各スイッチ
  judge = True
  for i in range(M):
    cnt = 0
    for j in range(1, len(q[i])): #range(1,x)は2番目から(K+1)-1番目まで
      w = q[i][j] #i番目のスイッチ,j番目の電球
      if s >> (w-1) & 1 == 1: # 右シフト
        cnt += 1
    if cnt % 2 != p[i]:
      judge = False
  if judge:
    ans += 1
print(ans)