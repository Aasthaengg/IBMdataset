import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    x = I()
    ans = 0
    cnt = 0

    while cnt<x:
        ans += 1
        cnt += ans

    print(ans)
    
main()            
