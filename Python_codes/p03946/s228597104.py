n,t=map(int,input().split())
s=list(map(int,input().split()))
mi=s[0]
ma=[]
for i in range(n):
    if s[i]<mi:
        mi=s[i]
    ma.append(s[i]-mi)
ma.sort()
print(ma.count(ma[-1]))
