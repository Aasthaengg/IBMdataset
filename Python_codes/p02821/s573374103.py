import sys
readline = sys.stdin.readline

N,M = map(int,readline().split())
A = list(map(int,readline().split()))

MAX_VAL = 10 ** 5 + 1
hand = [0] * MAX_VAL
for a in A:
  hand[a] += 1
  
import numpy as np
def convolve(f, g):
    fft_len = 1
    while 2 * fft_len < len(f) + len(g) - 1:
        fft_len *= 2
    fft_len *= 2
    
    Ff = np.fft.rfft(f, fft_len)
    Fg = np.fft.rfft(g, fft_len)

    Fh = Ff * Fg

    h = np.fft.irfft(Fh, fft_len)
    h = np.rint(h).astype(np.int64)

    return h[:len(f) + len(g) - 1]

right_hand = np.array(hand, dtype = int)
left_hand = np.array(hand, dtype = int)

H = convolve(left_hand, right_hand)
# Hを大きいほうから見ていくと、
# 幸福度iの握手をH[i]種類できることが分かる
# 上から順に足していって、最後H[i]種類の握手を足せないときは、残りの握手回数だけ足す

ans = 0
for i in range(len(H) - 1, -1, -1):
  if H[i] == 0:
    continue
  if H[i] <= M: # H[i]回の握手ができる
    ans += i * H[i]
    M -= H[i]
  else: # H[i]回の握手ができないので、残った回数だけ握手する
    ans += M * i
    break

print(ans)