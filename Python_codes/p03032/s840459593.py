N,K=map(int,input().split())
v=list(map(int,input().split()))
ans=0

for i in range(min(N,K)+1): #i個の宝石を得る
    for a in range(i+1): #左からa個の宝石を得る
        b=i-a #右からb個の宝石を得る
        val=sorted(v[:a]+v[N-b:]) #宝石の価値の合計
        s=sum(val)
#        print(val)
        for j in range(0,min(K-i,len(val))): #j個の宝石を捨てる、上限はk-iか得た宝石の個数i
            if j<len(val):
#                print("#",a,b,min(K-i,len(val)),val)
                if val[j]<0: #負の宝石を捨てる
                    s-=val[j]
            else:
                break
#        print(a,b,min(K-i,len(val)),val,sum(val))
        ans=max(ans,s)
print(ans)
