import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    a = LI()
    a.sort(reverse=True)
    ans = a[0]
    n -= 1
    for i in range(n-1):
        index = i//2 + 1
        ans += a[index]
    print(ans)
main()