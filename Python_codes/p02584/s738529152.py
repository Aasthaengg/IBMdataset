X, K, D = map(int, input().split())

# Xは0以上として一般性を失わない
X = abs(X)
ans = 0
# 「X-KD>=0」であれば、その地点で終了
# 「X-KD<0」であれば、原点周りを振動する
if X - K*D >= 0:
  ans = X - K*D
else:
  count = X // D
  K = K - (X // D) # math.floor() を使うより簡潔
  if K % 2 == 0: 
    ans = X - count*D
  else: 
    ans = D - (X - count*D)
    
print(ans)