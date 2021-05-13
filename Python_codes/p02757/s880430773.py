n,p=map(int,input().split())
s=input()
total=[0]*p#pで割った余りで分類
total[0]=1#t[0]=0の分をあらかじめカウント
t=[0]*(n+1)#s[i:n]を格納する用の配列
if p==2 or p==5:
    ans=0
    for i in range(n):
        if int(s[i])%p==0:
            ans+=i+1
    print(ans)
else:
    for i in range(n-1,-1,-1):
        t[i]=t[i+1]%p+int(s[i])*pow(10,n-1-i,p)#s[i:n]を漸化式で付け加えていく
        total[t[i]%p]+=1
    ans=0
    for i in range(p):
        ans+=total[i]*(total[i]-1)//2
    print(ans)