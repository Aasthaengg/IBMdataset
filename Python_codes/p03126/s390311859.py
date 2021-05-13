n,m=map(int,input().split())
s=set(range(m+1))
for i in range(n):s=s&set(list(map(int,input().split()))[1:])
print(len(s))