import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    # popするため逆順にしておく
    A=[list(map(lambda x:int(x)-1,input().split())) for _ in range(n)]
    for i in range(n): A[i].reverse()
    stack=[]

    def check(i):
        if(not A[i]): return
        j=A[i][-1]
        if(A[j][-1]==i):
            stack.append((min(i,j),max(i,j)))

    # calculate
    for i in range(n): check(i)
    day=0
    while(stack):
        day+=1
        stack=list(set(stack)) # uniqueを取る
        prev,stack=stack,[]
        for i,j in prev:
            A[i].pop(); A[j].pop()
        for i,j in prev:
            check(i); check(j)
    print(-1 if(any(A[i] for i in range(n))) else day)
resolve()