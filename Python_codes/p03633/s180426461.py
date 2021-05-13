import fractions

N=int(input())
S=[]
for i in range(N):
    S.append(int(input()))


def koubaisu(a,b):
    return a*b//fractions.gcd(a,b)

ans=1

if N==1:
    print(S[0])
    exit()
elif N==2:
    ans=koubaisu(S[0],S[1])
    print(ans)
    exit()
elif N>2:
    ans=koubaisu(S[0],S[1])
    for i in range(N-2):
        ans=koubaisu(ans,S[i+2])

print(ans)