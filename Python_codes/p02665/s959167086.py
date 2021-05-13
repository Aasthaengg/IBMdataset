# 初期入力
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
child =[0]*(N+1)
child[0] =2

#根→葉に向かって、子の最大値
if N ==0 :
    if A[0] ==1:
        child[0] =0
    else:
        print(-1)
        exit()

#A[0] ==0はエラー＝根は頂点１つ（N=0の時はOK)
else:
    if A[0] !=0:
        print(-1)
        exit()
    else:
        for i in range(1,N):
            child[i] =2*(child[i-1] -A[i])
            if child[i]<0: #子がマイナスはありえない
                print(-1)
                exit()

        #葉→根に向かって子と葉の関係を見る
        if child[N-1] *2 <A[N]:
            print(-1)
            exit()
        else:
            child[N-1] =min(A[N],child[N-1])
        for i in range(N-2,-1,-1):
            child[i] =min(child[i],child[i+1] +A[i+1] )

print(sum(child) +1) #根も頂点、＋１