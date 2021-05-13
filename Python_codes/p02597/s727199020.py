import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip.split())
def main():
    n = I()
    c = list(S())
    alldic = collections.Counter(c)
    allnum = alldic["R"]
    leftdic = collections.Counter(c[:allnum])
    leftnum = leftdic["R"]
    ans = allnum-leftnum
    print(ans)
main()