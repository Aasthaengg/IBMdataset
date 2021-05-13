n, t = map(int, input().split())
A = list(map(int, input().split()))
B = [0]

m = A[0]
for a in A[1:]:
  B.append(a - m)
  m = min(m, a)
  
mx = max(B)

ans = B.count(mx)
print(ans)