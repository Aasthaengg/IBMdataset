import itertools
N=int(input())
d=list(map(int,input().split()))
ls=[]
for i in range(N):
    ls.append(i)
lsp=list(itertools.permutations(ls,2))
#print(lsp)
ans=0
#print(lsp[])
for i in range(len(lsp)):
    ans += d[lsp[i][0]]*d[lsp[i][1]]
print(ans//2)
