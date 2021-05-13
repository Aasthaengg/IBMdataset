def ranlength(A):
    num = list(A)
    count = 1
    result = ''
    table = []
    for i in range(len(num)):
        try:
            if num[i] == num[i+1]:
               count = count + 1
            else:
                result += str(num[i]) + str(count)
                table.append(count)
                count = 1
        except:
            result += str(num[i]) + str(count)
            table.append(count)
    return(table)
    
N,K=map(int,input().split())
S=input()

RL=ranlength(S)
if S[0]=='0':
    RL=[0]+RL
if S[-1]=='0':
    RL.append(0)

#しゃくとり法
cnt=RL[0]
ans=RL[0]
for i in range(len(RL)):
    if i%2==0 and i>=2:
        cnt+=RL[i]
        cnt+=RL[i-1]
        if i>=K*2+2:
            cnt-=RL[i-(K*2+1)]
            cnt-=RL[i-(K*2+2)]
        ans=max(ans,cnt)
        #print(cnt)
print(ans)