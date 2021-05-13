import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())

N,A,B = MI()
C = A-B
h = [I() for i in range(N)]

def f(n):  # n回の爆発で討伐完了できるか
    a = 0
    for i in range(N):
        if h[i]-B*n > 0:
            a += (h[i]-B*n+C-1)//C
    if a <= n:
        return True
    else:
        return False

left = 0
right = 10**9
while left + 1 < right:
    mid = (left + right)//2
    if f(mid):
        right = mid
    else:
        left = mid

print(right)
