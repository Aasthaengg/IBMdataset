mod=10**9+7
n,k=map(int,input().split())
arr=list(map(int,input().split()))
cnt_plus=0
cnt_zero=0
cnt_minus=0
arr_plus=[]
arr_minus=[]

for i in range(n):
    if arr[i]>0:
        cnt_plus+=1
        arr_plus.append(arr[i])
    elif arr[i]<0:
        cnt_minus+=1
        arr_minus.append(-arr[i])
    else:
        cnt_zero+=1
if cnt_plus+cnt_minus<k: #K個の積の中に0を含む場合、答えは0
    print(0)
    exit()
    
if k==n: #K=Nの場合
    if cnt_zero!=0: #0がひとつでもあれば答えは0
        print(0)
    else:
        ans=1
        for i in range(cnt_plus):
            ans*=arr_plus[i]
            ans%=mod
        for i in range(cnt_minus):
            ans*=arr_minus[i]
            ans%=mod
        if cnt_minus%2==0: #負の数が偶数個であれば積は正
            print(ans)
        else: #そうでなければ積は負となる
            print((-ans)%mod)
    exit()
if cnt_plus==0 and k%2==1: #正の数がないとき
    if cnt_zero!=0: #0がひとつでもあれば答えは0にできる
        print(0)
    else: #0がないときは負の数を絶対値が小さい順に掛けるのが最善
        arr_minus=sorted(arr_minus)
        tmp=1
        for i in range(k):
            tmp*=arr_minus[i]
            tmp%=mod
        print((-tmp)%mod)
    exit()
else: #正の数と負の数から合計K個取れるとき
    arr_plus=sorted(arr_plus,reverse=True)
    arr_minus=sorted(arr_minus,reverse=True)
    if k%2==0: #Kが偶数であれば何もしない
        ans=1
        pos_plus=0
        pos_minus=0
        cnt=0
    else: #Kが奇数であれば正の数から最大のものを取っておき、Kが偶数の場合に帰着させる
        ans=arr_plus[0]
        pos_plus=1
        pos_minus=0
        cnt=1
    while cnt<k:
        cand1=0
        if pos_plus<=cnt_plus-2: #正の数を2つ取れるなら取る
            cand1=arr_plus[pos_plus]*arr_plus[pos_plus+1]      
            cand2=0
        if pos_minus<=cnt_minus-2: #負の数を2つ取れるなら取る:
            cand2=arr_minus[pos_minus]*arr_minus[pos_minus+1]
        if cand1>=cand2: #正の数を2つ取った積のほうが大きい場合
            pos_plus+=2
            ans*=cand1
            ans%=mod
        else: #負の数を2つ取った積のほうが大きい場合
            pos_minus+=2
            ans*=cand2
            ans%=mod
        cnt+=2
    print(ans)
    exit()
