import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
a,b,c = map(int,readline().split())
#a:美味しくない
#b:美味しい
#c:毒、美味しい

res = c-a
if res <= 0:
    print(b+c)
else:
    res = res-b
    if res <= 0:
        print(b+c)
    else:
        print(min(b+c,b+c-res+1))