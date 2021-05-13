import math
N, K = map(int,input().split())
logs = list(map(int,input().split()))


ng = 0##ngは常に条件を満たさないように設定
ok = max(logs)##okは常に条件を満たすように設定
while abs(ok-ng)>1:##absをとることで問題ごとにokとngの大小を考えなくてよくなる
  times = 0
  mid = (ok+ng)//2
  for A in logs:
    times += math.ceil(A/mid)-1
    
    
  if times <= K:
    ok = mid##条件を満たすならokを寄せる 
  else:
    ng = mid##満たさないならngを寄せる
    
print(ok)##今回はokそのまま答えだけど普通は添え字
