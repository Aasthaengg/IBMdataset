N,M=map(int,input().split())
#Sをすべて使うとき必要なCの数は2N
if M<2*N:
    print(M//2)
else:
    ans=N#現時点で作ったScc
    m=M-2*N#残りのc
    #Sccを１こ作るのにcは4つ必要
    ans+=m//4
    print(ans)