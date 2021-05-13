s=list(input().split())
L=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
l=list('abcdefghijklmnopqrstuvwxyz')
ans=''
for i in s:
    ans= ans+L[l.index(i[0])]
print(ans)