n=int(input())
ab=[list(map(int,input().split())) for _ in range(n)]

l=sorted([(a+b,a,b) for a,b in ab],reverse=True)

ans=sum([a for s,a,b in l[::2]])-sum([b for s,a,b in l[1::2]])

print(ans)