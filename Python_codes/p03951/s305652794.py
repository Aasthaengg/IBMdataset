# import string
import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    N=int(input())
    s=str(input())
    t=str(input())
    ans=2*N
    for i in range(1,N+1):
        #print(s[-i:])
        #print(t[:i])
        if s[-i:]==t[:i]:
            ans=2*N-i
    print(ans)



resolve()