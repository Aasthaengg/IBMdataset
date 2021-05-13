n=int(input())
a_list=list(map(int,input().split()))
pre1=[]
pre2=[]
for i in range(20):
    pre1.append(-1)
    pre2.append(-1)
ans=0
for i in range(n):
    Min=n
    s=format(a_list[i],'b').zfill(20)
    for j in range(20):
        if s[j]=='0':
            Num=i-pre2[j]
        else:
            Num=i-pre1[j]
            pre2[j]=pre1[j]
            pre1[j]=i
        Min=min(Min,Num)
    ans=ans+Min
print(ans)
    
