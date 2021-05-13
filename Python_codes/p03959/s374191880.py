N = int(input())
T = list(map(int,input().split()))
A = list(map(int,input().split()))
exact = [0] * N # 高さが確定した場所
seem = [0] * N # 高さが確定しない場所のあり得る最大値

cur = 0
for i in range(len(T)):
  if cur < T[i]:
    exact[i] = T[i]
    cur = T[i]
  else:
    seem[i] = cur
    
cur = 0
for i in range(len(A)-1,-1,-1):
  if cur < A[i]:
    if exact[i] != 0 and exact[i] != A[i]: # 既に記録された確定数値が今回の値と異なる場合
      print(0)
      exit(0)
    if exact[i] == 0 and seem[i] < exact[i]:# ここで確定させる数値が高橋くん的にあり得るかチェック
      print(0)
      exit(0)
    exact[i] = A[i]
    cur = A[i]
  else:
    # 既に確定している数値が今入れようとしている数値より大きければNG
    if exact[i] != 0 and exact[i] > cur:
      print(0)
      exit(0)
    seem[i] = min(seem[i],cur)
    
DIV = 10 ** 9 + 7
ans = 1
for i in range(N):
  if exact[i] != 0: # 確定数値があれば場合の数は変わらない
    continue
  else:
    ans *= seem[i]
    ans %= DIV

print(ans)