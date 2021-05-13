n,k = map(int,input().split())
V = list(map(int,input().split()))
Vi = V[::-1]
t = min(n,k)
ans = 0
for i in range(1,t+1):#選ぶ個数
    for a in range(0,i+1):
        b = i-a
        houseki = V[0:a] + Vi[0:b]
        houseki.sort()
        tmp=sum(houseki)
        for idx,val in enumerate(houseki):
            if idx==k-i:break
            if val<0:tmp-=val
        ans = max(ans,tmp)
print(ans)
