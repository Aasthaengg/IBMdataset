n=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
import itertools
dic={'M':0,'A':0,'R':0,'C':0,'H':0}
for i in range(n):
    s=input()
    dic[s[0]]=dic.get(s[0],0)+1
ans=0
pt=['M','A','R','C','H']
for v in itertools.combinations(pt,3):
    ans+=dic[v[0]]*dic[v[1]]*dic[v[2]]
print(ans)