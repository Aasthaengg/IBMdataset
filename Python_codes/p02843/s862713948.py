X=int(input())

ns=X//105
ne=X//100


ans=0
for i in range(ns, ne+1):
    if 100*i<=X<=100*i+5*i:
        ans=1
        break
print(ans)