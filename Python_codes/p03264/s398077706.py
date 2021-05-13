import itertools
K=list(itertools.combinations(range(1,int(input())+1),2))
c=0
for i in K:
    if (i[0]%2==0 and i[1]%2==1) or (i[0]%2==1 and i[1]%2==0):
        c+=1
print(c)