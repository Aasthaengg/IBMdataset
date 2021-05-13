import sys
import bisect

def main():
  input = sys.stdin.readline
  inf = pow(10, 18)
  a, b, q = map(int, input().split())
  s = [-inf]+[int(input()) for _ in range(a)]+[inf]
  t = [-inf]+[int(input()) for _ in range(b)]+[inf]
  
  for _ in range(q):
    x = int(input())
    i = bisect.bisect_left(s, x)
    j = bisect.bisect_left(t, x)
    ans = inf
    for l in range(-1, 1):
      for m in range(-1, 1):
        sub = min([abs(x-s[i+l]), abs(x-t[j+m])])+abs(s[i+l]-t[j+m])
        if ans > sub:
          ans = sub
    print(ans)

if __name__ == "__main__":
  main()