N, Q = map(int, input().split())
S = input()
A = []
a = 0
for i in range(N-1):
  if S[i] == 'A' and S[i+1] == 'C':
    a += 1
    A.append(a)
  else:
    A.append(a)
for i in range(Q):
  l, r = map(int, input().split())
  if l>=2:
    ans = A[r-2]-A[l-2]
    print(ans)
  else:
    ans = A[r-2]
    print(ans)