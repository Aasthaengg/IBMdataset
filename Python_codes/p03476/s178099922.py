memo =[1]*(10**5+1)
memo[0]=0
memo[1]=0
for i in range(2,len(memo)):
    if memo[i]==0:
        continue
    else:
        for j in range(i*2,len(memo),i):
            memo[j]=0
memo_like2017 = [0]*(10**5+1)
for i in range(3,len(memo),2):
    if memo[i]==1 and memo[(i+1)//2] ==1:
        memo_like2017[i]=1
sum_memo=[0]*(10**5+1)
for i in range(1,len(memo)):
    sum_memo[i] = sum_memo[i-1]+memo_like2017[i]

Q = int(input())
for _ in range(Q):
    l,r = map(int,input().split())
    print(sum_memo[r]-sum_memo[l-1])
