N,M = map(int,input().split())
A = list(map(int,input().split()))
A.sort(reverse=True)

#幸福度をX以上増やせる手が何通りあるか？を二分探索．
#左手で握る人は線形探索，右手が二分探索で探す
#最後は累積和で計算

inf = 2*10**5+1
X_top = inf
X_bot = 0 #M手以上の組み合わせが作れる最大値

#幸福度をX以上挙げられる手の通り数ががMになる境界を探す
while X_top - X_bot !=1:  
    X=(X_top+X_bot)//2
    num=0
    
    for i in range(N):
        ok=-1
        ng=N
        h1=A[i]
        
        #右手と左手の合計がXになる境界を探す
        while ng-ok!=1:
            med=(ok+ng)//2
            h2=A[med]
            if h1+h2>=X:
                ok=med
            else:
                ng=med
        num+=ok+1
    
    if num>=M:
        X_bot = X
    else:
        X_top = X
        
ok_list=[0]*N
#各左手に対して何個okなくみがあるか探す
for i in range(N):
        ok=-1
        ng=N
        h1=A[i]
        X = X_bot
        #右手と左手の合計がXになる境界を探す
        while ng-ok!=1:
            med=(ok+ng)//2
            h2=A[med]
            if h1+h2>=X:
                ok=med
            else:
                ng=med
        ok_list[i]=ok

S=[0]*(N+1)
for i in range(N):
    S[i+1]=S[i]+A[i]

ans=0
for i in range(N):
    ans += A[i]*(ok_list[i]+1)+S[ok_list[i]+1]

if sum(ok_list)+N>M:
    ans-=(sum(ok_list)+N-M)*X
print(ans)