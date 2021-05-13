N=int(input())
S1=input()
S2=input()
MOD=10**9+7

def ranlength(A):
    num = list(A)
    count = 1
    table = []
    for i in range(len(num)):
        try:
            if num[i] == num[i+1]:
               count = count + 1
            else:
                table.append(count)
                count = 1
        except:
            table.append(count)
    return(table)

T=ranlength(S1)
ans=T[0]*3
for i in range(1,len(T)):
    if T[i-1]==1:
        ans*=2
    elif T[i-1]==2 and T[i]==2:
        ans*=3
    ans%=MOD
print(ans)