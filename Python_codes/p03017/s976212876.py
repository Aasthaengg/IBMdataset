N,A,B,C,D=map(int,input().split())
S=input()

ans='Yes'
if '##'in S[A-1:C]:
    ans='No'
elif '##'in S[B-1:D]:
    ans='No'
elif C>D and ('...'not in S[B-2:D]):
    ans='No'
    if S[D-2]=='.' and S[D]=='.':
        ans='Yes'

print(ans)