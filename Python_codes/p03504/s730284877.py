from operator import itemgetter
N, C = list(map(int, input().split()))

BA = []
for i in range(N):
  BA.append(list(map(int, input().split())))

BA.sort(key=itemgetter(2,0,1))

# 0.5刻みのIMOS
IMO = [0] * (200010)
prev_c = -1
prev_t = -1
tmax = 0
for i in range(N):
  s, t, c = BA[i]
  if prev_c == c and prev_t == s:
    IMO[2*s+1] += 1
    IMO[2*t+1] -= 1
  else:
    IMO[2*s-1] += 1
    IMO[2*t+1] -= 1
    
  prev_t, prev_c = t,c
  tmax = max(tmax, t)
  
for i in range(2*tmax+5):
  IMO[i+1] += IMO[i]
  
print(max(IMO[:2*tmax+5]))
#print(IMO[:2*tmax+5])