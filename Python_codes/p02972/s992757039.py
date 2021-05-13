n = int(input())
a = list(map(int,input().split()))
box = [0]*n
for i in range(n,0,-1):
  k = a[i-1]
  c = 0
  for j in range(1,n//i+1):
    c += box[i*j-1]
  if c%2 != k:
    box[i-1] = 1
ans = []
w = 0
for m in range(n):
  if box[m] == 1:
    w += 1
    ans.append(str(m+1))
print(w)
print(' '.join(ans))