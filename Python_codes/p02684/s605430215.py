n,k=map(int,input().split())
a=list(map(int, input().split()))

logk = k.bit_length()
doubling = []
for _ in range(logk):
  tmp = [0] * n
  doubling.append(tmp)

for i in range(n):
  doubling[0][i] = a[i] - 1

for i in range(1,logk):
  for j in range(n):
    doubling[i][j] = doubling[i-1][doubling[i-1][j]]

now = 0
pos = 0
while k:
  if k & 1:
    now = doubling[pos][now]
  k = k >> 1
  pos += 1

print(now+1)
