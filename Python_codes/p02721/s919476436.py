ss = input().split()
n,k,c = map(int, ss)
s = input()

L = {}
R = {}

# forward
i = 0
fk = 0
while i < n and fk < k:
  if s[i] == 'x':
    i += 1
  else:
    L[fk+1] = i
    i += (c + 1)
    fk += 1
    

# backward
n -= 1
while 0 <= n and 0 < k:
  if s[n] == 'x':
    n -= 1
  else:
    R[k] = n
    n -= (c + 1)
    k -= 1


keys = set(L.keys()) | set(R.keys())
for k in sorted(keys):
  if k in R and k in L:
    if R[k] == L[k]:
      print(R[k]+1)
