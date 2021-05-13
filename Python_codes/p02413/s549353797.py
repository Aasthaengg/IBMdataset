r,c=map(int,raw_input().split())
l=[]
for i in range(r):l.append(map(int,raw_input().split()))
l.append([0]*(c+1))
for i in range(c+1):
    for j in range(r):
        if i==0:l[j].append(sum(l[j]))
        l[-1][i]+=l[j][i]
for i in range(r+1):print' '.join(map(str,l[i]))