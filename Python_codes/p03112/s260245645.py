import sys
 
read = sys.stdin.buffer.read
input = sys.stdin.buffer.readline
inputs = sys.stdin.buffer.readlines

def main():
  inf = float("INF")
  a,b,q = map(int, input().split())
  s = [None] * (a + 3)
  s[0:2] = [-inf,-inf]
  s[-1] = inf
  t = [None] * (b + 3)
  t[0:2] = [-inf,-inf]
  t[-1] = inf
  for i in range(a):
      s[i+2] = int(input())
  for i in range(b):
      t[i+2] = int(input())

  from bisect import bisect_right

  for _ in range(q):
    ans = inf
    x = int(input())
    sr = bisect_right(s, x)
    tr = bisect_right(t, x)    
    for si in (sr, sr-1):
      for ti in (tr, tr-1):
        ans = min(ans, abs(x-s[si]) + abs(s[si]-t[ti]), abs(x-t[ti]) + abs(s[si]-t[ti]))
    print(ans)
  
if __name__ == "__main__":
  main()
