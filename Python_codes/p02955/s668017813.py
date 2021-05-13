N, K = map(int, input().split())
A = [int(c) for c in input().split()]
S = sum(A)
pls = []
for i in range(1,S):
  if i*i>S:
    break
  if S%i==0:
    pls += [i]
    pls += [S//i]
pls.sort(reverse=True)
for p in pls:
    B = []
    for i in range(N):
      B += [A[i]%p]
    B.sort()
    for j in range(N):
      if B[j]!=0:
        break
    m = j
    lim = N-1
    cnt = 0
    while m<lim:
      if B[m]<p-B[-1]:
        B[-1] += B[m]
        cnt += B[m]
        B[m] = 0
        m += 1
      elif B[m]>p-B[-1]:
        cnt += p-B[-1]
        B[m] -= p-B[-1]
        B.pop()
        lim -= 1
      else:
        B.pop()
        cnt += B[m]
        B[m] = 0
        m += 1
        lim -= 1
    if B[-1]==0 and cnt<=K:
      print(p)
      break