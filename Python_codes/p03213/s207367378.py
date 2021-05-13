n=int(input())

N=[0]*(n+1)

def f(n):
    M=[]
    while n%2==0:
        n//=2
        M.append(2)
    i=3
    while n>=i:
        while n%i==0:
            n//=i
            M.append(i)
        i+=2
    return M

for i in range(2,n+1):
    for j in f(i):
        N[j]+=1

ANS=[0]*5

for i in range(1,n+1):
    if N[i]>=74:
        ANS[0]+=1
    elif N[i]>=24:
        ANS[1]+=1
    elif N[i]>=14:
        ANS[2]+=1
    elif N[i]>=4:
        ANS[3]+=1
    elif N[i]>=2:
        ANS[4]+=1

ANS[1]+=ANS[0]
ANS[2]+=ANS[1]
ANS[3]+=ANS[2]
ANS[4]+=ANS[3]

print(ANS[0]+ANS[1]*(ANS[4]-1)+ANS[2]*(ANS[3]-1)+(ANS[3]*(ANS[3]-1)//2)*(ANS[4]-2))