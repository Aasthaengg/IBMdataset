N=int(input())
S=input()
T='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans=''
for s in S:
    ans+=T[T.index(s)+N-26]
print(ans)