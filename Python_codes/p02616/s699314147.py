#正の場合、0の場合、負の場合で分ける
#負の数のみの場合は調整しようがない
#偶数の時は絶対値の大きい順
#奇数の時は絶対値の小さい順
#正の数のみの場合は大きい順
#大きい順

#他は調整できるので、正で大きくする方向で考える(正→0以上)
#負の数は偶数個ないと正にならないので二つ一組で先にかけて考える
#正の数も同様に先にかけて、その中で大きいものを選べば良い

#負の数が奇数個、正の数が奇数個の時(負の数が余る、正の数が余る)
#Kが偶数の時はいい感じに選んでく(N=kの時は仕方ないので全部)
#Kが奇数の時は正の中で最大のものを選ぶ
#負の数が偶数個、正の数が奇数個の時(正の数が余る)
#Kが偶数の時はいい感じに選んでく
#奇数の時は残りの正の中から選ぶ
#負の数が奇数個、正の数が偶数個の時(負の数が余る)
#N=Kの時は全部選ぶ、それ以外の場合は余った負の数はいらない
#Kが奇数の時は残りの正の中で最大のものを選べば良い
#負の数が偶数個、正の数が偶数個の時
#Kが奇数の時は残りの正の中で最大のものを選べば良い

#N=Kの時は別で分けて考えるとすると、負の数及び正の数によらず
#Kが偶数の時は大きいものからいい感じに選んでく
#Kが奇数の時は最後の残り一個は正の残りの中で最大のものを選ぶ
#と簡単に言い換えることができる

#x:配列
mod=10**9+7
def multarray(x):
    ret=1
    for i in x:
        ret*=i
        ret%=mod
    return ret

n,k=map(int,input().split())
a=list(map(int,input().split()))

if n==k:
    print(multarray(a))
    exit()

ap,am=[],[]
for i in range(n):
    if a[i]>=0:
        ap.append(a[i])
    else:
        am.append(a[i])
#絶対値の順番
ap.sort(reverse=True)
am.sort()

if len(am)==0:
    print(multarray(ap[:k]))
    exit()
if len(ap)==0:
    if k%2==0:
        print(multarray(am[:k]))
    else:
        print(multarray(am[::-1][:k]))
    exit()

apm2=[]
for i in range(len(am)//2):
    apm2.append((am[2*i]*am[2*i+1],0))
for i in range(len(ap)//2):
    apm2.append((ap[2*i]*ap[2*i+1],1))
apm2.sort(reverse=True)

#+の次にどこを見るのかをチェックしておく
#まだかけない
p=0
ans=[]
for i in range(k//2):
    p+=(2*apm2[i][1])
    ans.append(apm2[i][0])

#ここで不正アクセスの可能性を避ける
#プラスが余ってない場合(一個減らして次のマイナス使う)
if k%2==0:
    print(multarray(ans))
    exit()
if p==len(ap):
    #一個減らす
    check_i=ans.index(ap[p-1]*ap[p-2])
    ans[check_i]=ap[p-2]
    ans.append(apm2[k//2][0])
    print(multarray(ans))
else:
    #余ってる場合もafter_contestで落ちる
    #その一個をとるのが最適とは限らない
    #一個減らして二個とる場合も
    ans_cand=[]
    #一個増やす場合
    ans_cand.append(multarray(ans)*ap[p]%mod)
    if p>=2:
        #一個減らして二個増やす場合
        check_i=ans.index(ap[p-1]*ap[p-2])
        #0除算を避ける
        ans[check_i]=ap[p-2]
        ans.append(apm2[k//2][0])
        ans_cand.append(multarray(ans))
    print(max(ans_cand))
