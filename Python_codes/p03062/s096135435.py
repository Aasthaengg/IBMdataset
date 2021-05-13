n = int(input())
ls = list(map(int,input().split()))
p = 0
k = float("inf")
q = 0
for i in range(n):
  p += abs(ls[i])
  if k > abs(ls[i]):
    k = abs(ls[i]) 
di = [e for e in ls if e <= 0]
if len(di) % 2== 0:
  print(p)
else:
  print(p-2*k)