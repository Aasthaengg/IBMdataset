import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    N=int(input())
    results=[]
    for i in range(1,N):
        results.append(sum(map(int,str(i)))+sum(map(int,str(N-i))))
    print(min(results))
    


resolve()