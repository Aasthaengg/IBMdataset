import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
input = sys.stdin.readline
mod = 10**9+7
Max = sys.maxsize
def l(): #intのlist
  return list(map(int,input().split()))
def m(): #複数文字
  return map(int,input().split())
def onem(): #Nとかの取得
  return int(input())
def s(x): #圧縮
  a = []
  if len(x) == 0:
    return []
  aa = x[0]
  su = 1
  for i in range(len(x)-1):
    if aa != x[i+1]:
      a.append([aa,su])
      aa = x[i+1]
      su = 1
    else:
      su += 1
  a.append([aa,su])
  return a
def jo(x): #listをスペースごとに分ける
  return " ".join(map(str,x))
def max2(x): #他のときもどうように作成可能
  return max(map(max,x))
def In(x,a): #aがリスト(sorted)
    k = bs.bisect_left(a,x)
    if k != len(a) and a[k] ==  x:
        return True
    else:
        return False

def pow_k(x, n):
    ans = 1
    while n:
        if n % 2:
            ans *= x
        x *= x
        n >>= 1
    return ans

"""
def nibu(x,n,r):
  ll = 0
  rr = r
  while True:
    mid = (ll+rr)//2

  if rr == mid:
    return ll
  if (ここに評価入れる):
    rr = mid
  else:
    ll = mid+1
"""

n,k = m()

if n == 0:
  if k == 0:
    print("0 0")
  else:
    print(-1)

elif n == 1:
  if k == 0:
    print("0 0 1 1")
  else:
    print(-1)
else:
  if 2<<(n-1) > k:
    po = []

    op = []

    for i in range((2<<(n-1))):
      if i == k:
        continue
      else:
        if po == "":
          po.append(i)
          op.append(i)
        else:
          po.append(i)
          op.append(i)
    op.reverse()
    print("{0} {1} {2} {3}".format(jo(po),k,jo(op),k))
  else:
    print(-1)

