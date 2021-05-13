#
def div(n): #約数を求める
 ret=[]
 for i in range(1,int(n**0.5)+1):
   if n%i==0:
     ret.append(i)
     if i!=n//i:
       ret.append(n//i)
 return ret

n,k=map(int,input().split())
arr=list(map(int,input().split()))
ans=1
d=div(sum(arr))
for val in d: #すべての約数について条件判定
 arr=sorted(arr,key=lambda x:x%val) #配列を、約数で割ったあまりが小さい順にソート
 parr=[] #配列の各要素を(x-arr[i]%x)足すときの操作回数
 narr=[] #配列の各要素をarr[i]%x引くときの操作回数
 for num in arr:
   narr.append(num%val)
   parr.append(val-num%val)
 for i in range(n-1): #上記の値の累積和を取る
   parr[i+1]+=parr[i]
   narr[i+1]+=narr[i]
 for i in range(n-1): #累積和を用いて条件判定
   ncnt=narr[i] #左からi番目の要素まで、各要素が約数の倍数になるように値を引くときの操作回数
   pcnt=parr[-1]-parr[i] #左からi+1番目の要素から右端の要素まで、各要素が約数の倍数になるように値を足すときの操作回数
   if ncnt!=pcnt: #足す回数と引く回数が一致していなければそもそも操作は不可能
     continue
   else:
     if pcnt<=k: #操作回数がK以下であればその約数は答えの候補になる
       ans=max(ans,val)
print(ans) #答えの候補となる約数の最大値が答えとなる
