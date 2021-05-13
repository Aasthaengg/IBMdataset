import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    answer=1
    n=int(input())
    for i in range(1,n+1):
        answer*=i
        answer%=10**9+7
    print(answer)
resolve()