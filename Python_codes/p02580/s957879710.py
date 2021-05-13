# https://atcoder.jp/contests/abc176/submissions/16124424
from collections import Counter
def abc176_e():
  h, w, m = map(int, input().split())
  H = []
  W = []
  for _ in range(m):
    hi, wi = map(int, input().split())
    H.append(hi)
    W.append(wi)
  mosth = Counter(H).most_common()[0]
  mostw = Counter(W).most_common()[0]
  ans1 = mosth[1]
  ans2 = mostw[1]
  wpair = []
  hpair = []
  for i, hi in enumerate(H):
    if hi == mosth[0]: continue
    wpair.append(W[i])
  for i, wi in enumerate(W):
    if wi == mostw[0]: continue
    hpair.append(H[i])
  if wpair:
    ans1 += Counter(wpair).most_common()[0][1]
  if hpair:
    ans2 += Counter(hpair).most_common()[0][1]
  ans = max(ans1, ans2)
  print(ans)

if __name__ == '__main__':
    abc176_e()