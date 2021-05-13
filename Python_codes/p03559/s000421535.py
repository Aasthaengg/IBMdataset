import bisect
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
C.sort()
lenC = len(C)

# Bを止めて,条件を満たすA,Cを数える。足し合わせる。
ans = 0
for b in B:
  idxA = bisect.bisect_left(A, b)
  idxC = lenC - bisect.bisect_right(C, b)
  ans += idxA * idxC
print(ans)