n,l = map(int,input().split())

D=[]
for i in range(n):
    d = l+i
    D.append(d)

if l+1>0 :
    mind = min(D)
elif l+n<=0:
    mind = max(D)
else:
    mind = 0


ans = sum(D)-mind
print(ans)

