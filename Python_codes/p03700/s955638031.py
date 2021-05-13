import sys
input = sys.stdin.readline

N, A, B = list(map(int, input().split()))
C = A-B
H = [int(input()) for _ in range(N)]

def check(K):
  s = 0
  D = K*B
  for h in H: s += max(0, (h-D+C-1)//C)
  return s<=K

max_NG = 0
min_OK = 10**10
while min_OK - max_NG > 1:
  tgt = (max_NG+min_OK)//2
  if check(tgt):
    min_OK = tgt
  else:
    max_NG = tgt

print(min_OK)