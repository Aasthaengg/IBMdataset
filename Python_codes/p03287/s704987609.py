N,M = map(int,input().split())
A = list(map(int,input().split()))

csum = [0]
for a in A:
  csum.append(csum[-1]+a)
#print(csum)

MOD = {}
for c in csum:
  m = c%M
  if m in MOD:
    MOD[m] += 1
  else:
    MOD[m] = 1
#print(MOD)

ans = 0
for _,v in MOD.items():
  if v >= 2:
    ans += v*(v-1)//2
print(ans)
