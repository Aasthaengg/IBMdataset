import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    s = S()
    k = min(len(s),I())

    ans = 1

    for i in range(k):
        if s[i] != "1":
            ans = s[i]
            break

    print(ans)
main()
