n=int(input())
da=[input() for i in range(3)]
ans=0
for i in range(n):
    ans+=len(set([da[0][i],da[1][i],da[2][i]]))-1
print(ans)