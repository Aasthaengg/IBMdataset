import sys
import math
readline = sys.stdin.readline

def main():
  p = 1000000007
  N = int(readline().strip())
  A = {}
  ans = 0
  for i in range(N):
    s = ''
    ai, bi = map(int, readline().split())
    if ai == 0 and bi == 0:
      ans += 1
      ans %= p
      continue
    gi = math.gcd(ai, bi)
    ai //= gi
    bi //= gi
    if ai != 0 and bi != 0:
      if ai < 0 and bi < 0:
        ai *= -1
        bi *= -1
      elif ai < 0:
        ai *= -1
        s = '-'
      elif bi < 0:
        bi *= -1
        s = '-'
    elif ai == 0 and bi != 0:
      ai = 0
      bi = 1
    elif bi == 0 and ai != 0:
      ai = 1
      bi = 0
      s = '-'
    xi = s + str(ai) + '/' + str(bi)
    if s == '':
      s = '-'
    else:
      s = ''
    yi = s + str(bi) + '/' + str(ai)
    if xi in A:
      A[xi][0] += 1
      A[xi][0] %= p
    elif yi in A:
      A[yi][1] += 1
      A[yi][1] %= p
    else:
      A[xi] = [1, 0]
  r = 1
  for i in A:
    r *= (pow(2, A[i][0], p) + pow(2, A[i][1], p) -1)
    r %= p
  ans += r - 1
  ans %= p
  print(ans)

if __name__ == '__main__':
  main()