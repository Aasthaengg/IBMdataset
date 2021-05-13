k,s=map(int,input().split())
c=0

for l in range(k+1):
    for m in range(k+1):
        if 0<=s-l-m and s-l-m<=k:
            c+=1
print(c)