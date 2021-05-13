def query(x):
    cnt=0
    while(x>0):
        x=x%bin(x).count('1')
        cnt+=1
    return cnt

N=int(input())
X=input()[::-1]
c=X.count('1')

sump,summ=0,0
for i in range(N):
    if X[i]=='1':
        sump=(sump+pow(2,i,c+1))%(c+1)
        if c>1:
            summ=(summ+pow(2,i,c-1))%(c-1)
ans=[]
for i in range(N):
    if X[i]=='0':
        x=(sump+pow(2,i,c+1))%(c+1)
        ans.append(query(x)+1)
    else:
        if c==1:
            ans.append(0)
        else:
            x=(summ-pow(2,i,c-1)+c-1)%(c-1)
            ans.append(query(x)+1)
print(*ans[::-1],sep='\n')