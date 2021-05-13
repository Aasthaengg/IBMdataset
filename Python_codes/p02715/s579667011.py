n,k=map(int,input().split())

mod=10**9+7

pow_table={}
def eco_pow(x):
    if x in pow_table:
        return pow_table[x]
    else:
        pow_table[x]=pow(x,n,mod)
        return pow_table[x]
    
ans=0
res_dic={}
for i in range(k):
    now=k-i
    all_now_res=eco_pow(k//now)
    del_now_res=0

    for q in range(2*now,k+1,now):
        #print(now,q)
        del_now_res+=res_dic[q]

    res_dic[now]=(all_now_res-del_now_res)%mod
    #print(res_dic[now])
    ans+=res_dic[now]*now
    ans%=mod

print(ans)