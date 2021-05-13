n, c = map(int, input().split())
stc = [list(map(int, input().split())) for _ in range(n)]

# 同チャンネルの連続する放送を一つにまとめる
stc.sort(key=lambda x: (x[2], x[0]))
 
imos = [0] * (10**5 + 1)

curr_c = 0
curr_t = 0
for s, t, c in stc:
  if curr_c == c and curr_t == s:
    imos[s] += 1
  else:
    imos[s-1] += 1
  imos[t] -= 1
  curr_t = t
  curr_c = c
  
rui = [0] * (10**5 + 1)

for i in range(10**5):
  rui[i+1] = rui[i] + imos[i]
  
print(max(rui))
