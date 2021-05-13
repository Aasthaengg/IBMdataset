N = int(input())
As = list(map(int, input().split()))

sm = []
tmp = 0
for a in As:
  tmp += a
  sm.append(tmp)
  
rlt = sum(map(abs, As))
for i in range(N-1):
  rlt = min(rlt, abs(2*sm[i]-sm[-1]))
  
print(rlt)