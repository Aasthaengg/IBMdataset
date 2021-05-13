import numpy as np
MOD = 10**9 + 7

def fft_convolve(f, g):
  Lf, Lg = f.shape[-1], g.shape[-1]
  L = Lf + Lg - 1
  fft_len = 1 << L.bit_length()
  fh, fl = f >> 15, f & (1 << 15) - 1
  gh, gl = g >> 15, g & (1 << 15) - 1
  def conv(f, g):
    Ff = np.fft.rfft(f, fft_len)
    Fg = np.fft.rfft(g, fft_len)
    h = np.fft.irfft(Ff * Fg)
    return np.rint(h)[..., :L].astype(np.int64) % MOD
  x = conv(fl, gl)
  z = conv(fh, gh)
  y = conv(fl + fh, gl + gh) - x - z
  return (x + (y << 15) + (z << 30)) % MOD

s = input()
x, y = map(int, input().split())

Rob = list(s.split("T"))

X = [len(r) for r in Rob[::2]]
Y = [len(r) for r in Rob[1::2]]

Xst = X[0]
X = X[1:]

if abs(x-Xst) <= sum(X) and abs(y) <= sum(Y):
  f = np.array([1], np.int64)
  for i in X:
    L = [0]*(2*i+1)
    L[0], L[-1] = 1, 1
    f = np.convolve(f, np.array(L, np.int64))
  FlagX = f[abs(x-Xst)+sum(X)]

  g = np.array([1], np.int64)
  for j in Y:
    L = [0]*(2*j+1)
    L[0], L[-1] = 1, 1
    g = np.convolve(g, np.array(L, np.int64))
  FlagY = g[abs(y)+sum(Y)]

  if FlagX and FlagY:
    print("Yes")
  else:
    print("No")
else:
  print("No")