import sys
readline = sys.stdin.readline

N,M = map(int,readline().split())

# Mの約数Pのうち、M // P >= Nとなるものの最大値

ans = 0
for i in range(1,int(M ** 0.5) + 1):
  if M % i == 0:
    p = M // i
    if i >= N:
      if ans < p:
        ans = p
    if p >= N:
      if ans < i:
        ans = i

print(ans)
