import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input():
    return sys.stdin.readline().rstrip()

def main():
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    A.sort()
    for a in A:
        if a==3:
            try:
                A.remove(2)
            except:
                pass
        elif a==5:
            try:
                A.remove(2)
            except:
                pass
            try:
                A.remove(3)
            except:
                pass
        elif a==9:
            try:
                A.remove(6)
            except:
                pass
    d={1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
    l=[d[x] for x in A]
    dp=[[0]*(N+1) for _ in range(len(l)+1)]
    prev_w=[[0]*(N+1) for _ in range(len(l)+1)]
    real_w=[[0]*(N+1) for _ in range(len(l)+1)]
    for num in range(len(l)):
        for w in range(N+1):
            if w>=l[num]:
                if dp[num+1][w]<dp[num+1][w-l[num]]+1 and real_w[num+1][w-l[num]]+l[num]==w:
                    dp[num+1][w]=dp[num+1][w-l[num]]+1
                    prev_w[num+1][w]=w-l[num]
                    real_w[num+1][w]=w
            if dp[num+1][w]<dp[num][w]:
                dp[num+1][w]=dp[num][w]
                prev_w[num+1][w]=w
                real_w[num+1][w]=w
    l2=[]
    cur_w=N
    for num in range(len(l)-1,-1,-1):
        while True:
            if prev_w[num+1][cur_w]==cur_w-l[num]:
                l2.append(str(A[num]))
                cur_w=prev_w[num+1][cur_w]
            else:
                cur_w=prev_w[num+1][cur_w]
                break
    print(''.join(l2))

if __name__ == '__main__':
    main()
