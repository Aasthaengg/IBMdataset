import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n,k = map(int,readline().split())

if (n+1)//2 >= k:
    print("YES")
else:
    print("NO")