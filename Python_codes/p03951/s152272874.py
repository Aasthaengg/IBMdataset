import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    s = S()
    t = S()

    lenth = 0

    for i in range(1,n+1):
        s_end = s[-i:]
        t_start = t[:i]

        if s_end == t_start:
            lenth = i
    
    ans = 2*n - lenth
    print(ans)
        
main()            
