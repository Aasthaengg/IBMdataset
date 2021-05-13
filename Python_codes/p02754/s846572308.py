n,a,b = map(int,input().split())
m = a+b
print(a*(n//m)+min(a,n-((n//m)*m)))