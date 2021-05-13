import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    k = I()
    ans = -1
    s = 7%k
    if s==0:
        ans = 1
    else:
        for i in range(1,k):
            s = (s*10+7)%k
            if s == 0:
                ans = i+1
                break
    print(ans)

main()            
