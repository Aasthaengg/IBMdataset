A,B,K = map(int,input().split())
count = 0
for i in range(100):
  if count ==K:
    break
  else:
    if A%2 == 1:
      A = A-1
    B = B + A/2
    A = A/2
    count += 1
  if count == K:
    break
  else:
    if B%2 == 1:
      B = B-1
    A = A+ B/2
    B = B/2
    count += 1
print(int(A),int(B))