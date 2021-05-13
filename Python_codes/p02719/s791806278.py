n,m=map(int,input().split())
s=n-((n//m)*m)
c=abs(s-m)
print(min(s,c))
