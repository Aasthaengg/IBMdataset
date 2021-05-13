N = int(input())
A = list(map(int,input().split()))

MOD = 1000000007

#色ごとの人数
C=[0,0,0]
ans=1
for a in A:
    #人数が一致する色がなければOUT
    found=False
    count=C.count(a)
    if count==0:
        print(0)
        exit()
    #適当に1人足す
    C[C.index(a)]+=1
    #今見ている人の色の可能性はcount種類
    ans=ans*count%MOD

print(ans)