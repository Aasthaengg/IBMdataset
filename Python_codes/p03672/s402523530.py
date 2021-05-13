import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    s = S()
    cut = 1 if len(s)%2==1 else 2
    scut = s[:-cut]
    # print(scut)

    while scut[:len(scut)//2] != scut[len(scut)//2:]:
        cut += 2
        scut = s[:-cut]

    ans = len(scut)
    print(ans)


main()