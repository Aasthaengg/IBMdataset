import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip.split())
def main():
    n = I()
    f_inf = float("inf")
    b = [f_inf] + LI() + [f_inf]

    a = [0 for _ in range(n)]
    for i in range(n):
        a[i] = min(b[i],b[i+1])
    ans = sum(a)
    print(ans)

main()