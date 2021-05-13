N,K = map(int,input().split())

ans_sum=0#確率合計

for i in range(1,N+1):
    num=i#現在の数字格納用
    ans=1/N #Nの目が出る確率
    while num<K:
        num*=2
        ans/=2
    #print(ans)
    ans_sum+=ans
print(ans_sum)