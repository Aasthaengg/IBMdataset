import bisect

X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

YZ = Y*Z
BC = []
for b in B:
  for c in C:
    BC.append(b+c)

BC.sort()
# 2つのリストから1つずつ要素を取り出したときに和がx以上となる組合せ
def count_large_2(L1, L2, x):
  L1.sort()
  L2.sort(reverse=True)
  N1, N2 = len(L1), len(L2)
  i = j = 0
  c = 0
  while i<N1 and j<N2:
    if L1[i]+L2[j] >= x:
      c += 1
      j += 1
      if j >= N2:
        c += (N1-i-1) * N2
    else:
      i += 1
      if i>=N1:
        continue
      c += j
  return c


def check(S):
  c = count_large_2(BC, A, S)  
  return c >= K



Sl = 0
Sr = A[0]+B[0]+C[0]+1

while Sr - Sl > 1:
  mid = (Sl + Sr) // 2
  if check(mid):
    Sl = mid
  else:
    Sr = mid


Ans = []
for a in A:
  for b in B:
    if a + b + C[0] < Sr:
      break
    for c in C:
      if a + b + c >= Sr:
        Ans.append(a+b+c)
      else:
        break

Ans.sort(reverse=True)
Ans = Ans + [Sl]*(K-len(Ans))
for ans in Ans:
  print(ans)