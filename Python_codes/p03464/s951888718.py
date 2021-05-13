K = int(input())
A = list(map(int, input().split()))

def is_ok(arg,flg):
  # 条件を満たすかどうか？問題ごとに定義
  N0 = arg
  for a in A:
    N0 -= N0 % a
  if flg:
    return  N0 >= 2
  else:
    return  N0 <= 2
    
def meguru_bisect(ng, ok, flg):
  '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
  '''
  while (abs(ok - ng) > 1):
    mid = (ok + ng) // 2
    if is_ok(mid, flg):
      ok = mid
    else:
      ng = mid
    #print(ok,ng)
  return ok
      
ok,ng = K * max(A) + 100, -1
m = meguru_bisect(ok,ng,False)
#print()
ok,ng = 0, K * max(A) + 100
M = meguru_bisect(ok,ng,True)

if M <= m:
  print(M,m)
else:
  print(-1)