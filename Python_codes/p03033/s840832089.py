import sys
input = sys.stdin.readline

def bs(d, x):
  l, r = 0, len(d)
  while l < r:
    mid = (l + r) // 2
    if d[mid] < x:
      l = mid + 1
    else:
      r = mid
  return l


def main():
  n, q = map(int, input().split())
  stx = [tuple(map(int, input().split())) for _ in range(n)]
  stx = list(sorted(stx, key=lambda x: x[2]))
  dlist = [int(input()) for _ in range(q)]
  ans = [-1 for _ in range(q)]
  skip = [-1 for _ in range(q)]
  for s, t, x in stx:
    l = bs(dlist, s-x)
    r = bs(dlist, t-x)
    while l < r:
      if skip[l] == -1:
        ans[l] = x
        skip[l] = r
        l += 1
      else:
        l = skip[l]
  print(*ans, sep='\n')


if __name__ == '__main__':
  main()