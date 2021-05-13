N = int(input())
jisyo = {}
for i in range(N):
  a = input()
  if a not in jisyo:
    jisyo[a] = 1
  else:
    jisyo[a] +=1
M = int(input())
for i in range(M):
  b = input()
  if b not in jisyo:
    jisyo[b] = -1
  else:
    jisyo[b] -=1
maxi = 0
for i,k in jisyo.items():
  if maxi < k:
    maxi = k
print(maxi)