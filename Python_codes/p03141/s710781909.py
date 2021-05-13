n=int(input())
ab=[list(map(int,input().split())) for _ in range(n)]
abc=[[a,b,a+b] for a,b in ab]
abc.sort(key=lambda x:x[2],reverse=True)
tk=sum([abc[0] for i,abc in enumerate(abc) if i%2==0])
ao=sum([abc[1] for i,abc in enumerate(abc) if i%2==1])
print(tk-ao)
