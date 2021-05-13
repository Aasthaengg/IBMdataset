n=int(input())
p=list(map(int,input().split()))
c=0

for i in range(n-2):
    if p[i+1]!=min(p[i:3+i]) and p[i+1]!=max(p[i:3+i]):
        c+=1
    elif p[i+1]==max(p[i:3+i]) and p[i:3+i].count(p[i+1])==2:
        c+=1
print(c)