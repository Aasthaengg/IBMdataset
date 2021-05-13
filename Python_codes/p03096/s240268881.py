import sys
sys.setrecursionlimit(2000000000)
input=lambda : sys.stdin.readline().rstrip('\n')

n=int(input())
dic={}
c=[0]
for i in range(n):
    t=int(input())
    if c[-1]!=t:
        c.append(t)
g=[[i+1] for i in range(len(c)-1)]
g.append([])
for i in range(len(c)):
    if c[i] in dic:
        g[dic[c[i]]].append(i)
        dic[c[i]]=i
    else:
        dic[c[i]]=i
ans_table=[0 for i in range(len(c))]
ans_table[-1]=1
for i in range(len(c)-1):
    i=len(c)-2-i
    for to in g[i]:
        ans_table[i]+=ans_table[to]
print(ans_table[0]%(10**9+7))