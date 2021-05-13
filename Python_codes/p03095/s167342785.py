alphabetlist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

N=int(input())
S=input()

dic={moji:0 for moji in alphabetlist}
for i in range(N):
    dic[S[i]]+=1

ans=1
mod=10**9+7
for moji in dic:
    ans*=dic[moji]+1
    ans%=mod

ans-=1
ans%=mod
print(ans)