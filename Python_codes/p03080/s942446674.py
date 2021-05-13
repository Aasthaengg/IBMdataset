import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    N=int(input())
    s=str(input())
    cnt=0
    for i in range(N):
        if s[i]=='R':
            cnt+=1
    print('Yes' if cnt>N-cnt else 'No')
    
resolve()