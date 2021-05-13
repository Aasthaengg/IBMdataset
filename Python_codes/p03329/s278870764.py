########10進法からn進法への変換関数部分##############
def Format(X, n):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)
    return out
############################

n=int(input())
# 6進表現と9進表現を全探索
ans=n
for i in range(n+1):
  j=n-i
  i,j=Format(i,6),Format(j,9)
  t=0
  for s in i:
    t+=int(s)
  for s in j:
    t+=int(s)
  ans=min(ans,t)
print(ans)