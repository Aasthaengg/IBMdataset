import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    A=LI()
    from collections import defaultdict
    dd = defaultdict(int)
    
    for i in range(N):
        dd[A[i]]+=1
        
    eat=0
    for k,v in dd.items():
        if v!=1:
            eat+=v-1
    if eat%2==1:
        eat+=1        
    
    print(N-eat)

main()
