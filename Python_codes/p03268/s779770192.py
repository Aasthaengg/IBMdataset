N,K = map(int,input().split())

# 1からNまでにmodKでiとなるものがいくつあるか数えておく。
num = [0 for _ in range(K)]
for i in range(1,N+1):
  num[i%K] += 1

ans = 0
# aを決め打ちすると、a+b=0modK,c+a=0modKよりb,cが定まる。
# それがb+c=0modKを満たすかチェックする。
for a in range(K):
  b = (K-(a%K))%K
  c = (K-(a%K))%K
  if (b+c)%K != 0:
    continue
  ans += num[a]*num[b]*num[c]
print(ans)