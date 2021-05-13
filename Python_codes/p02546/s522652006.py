S=list(input())
n=int(len(S))
ans=''
if S[n-1]=='s':
        ans=''.join(S)+'es'
else:
        ans=''.join(S)+'s'

print(ans)

