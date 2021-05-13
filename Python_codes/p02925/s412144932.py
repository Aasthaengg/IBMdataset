import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    M=[None]*n
    for i in range(n):
        M[i]=list(map(lambda x:int(x)-1,input().split()))[::-1]

    # i が誰かしらと対戦できるか
    def check(i):
        if(not M[i]): # 既に試合を終えている
            return False
        j=M[i][-1]
        if(not M[j]): # これは起こり得ない
            return False
        return i==M[j][-1]

    # 初日に対戦できる人をピックアップ
    # 重複が起こるが、後で unique を取る
    Q=[]
    for i in range(n):
        if(check(i)):
            j=M[i][-1]
            if(i>j): i,j=j,i # i<j
            Q.append((i,j))

    # 処理を行なっていく
    day=0
    nQ=[] # 次の試合相手
    while(Q):
        # Q には重複があるので unique
        Q=list(set(Q))
        # 先に全ての試合を終わらせる必要がある
        for i,j in Q:
            M[i].pop(); M[j].pop()
        # 試合を終えた人は次の試合を行える可能性がある
        for i,j in Q:
            if(check(i)):
                k=M[i][-1]
                nQ.append((min(i,k),max(i,k)))
            if(check(j)):
                k=M[j][-1]
                nQ.append((min(j,k),max(j,k)))
        Q,nQ=nQ,[]
        day+=1

    print(day if(all(M[i]==[] for i in range(n))) else "-1")
resolve()
