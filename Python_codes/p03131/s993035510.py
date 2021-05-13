#みんなのプロコン2019-C
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

k,a,b = map(int,readline().split())

if b-a <= 2:
    print(k+1)
    exit()

res = max(0,(k-(a-1))//2)

ans = a+res*(b-a)

if not even(k-(a-1)):
    ans += 1

print(ans)