#入力を受け取る
N,K=map(int,input().split())
a=list(map(int,input().split()))
#grundy[k]:=山にk(1≤k≤K)個石がある時のgrundy数
grundy=[0]*(K+1)
#DP(動的計画法)の考えかたを用いてGrundy数を求める
for j in range(K+1):
    s=set()
    for i in range(N):
        if a[i]<=j:
            s.add(grundy[j-a[i]])
    #mex()の動作
    g=0
    while g in s:g+=1 
    grundy[j]=g
if grundy[K]:print("First")
else:print("Second")

