n,m=map(int,input().split())

d={}
for i in range(m):
    p,y=map(int, input().split())
    if p not in d:
        d[p]=[[y,p,i]]
    else:
        d[p].append([y,p,i])

bango_list=['0']*m
for key in d:
    d[key].sort()
    for i in range(len(d[key])):
        p_bango=str(key).zfill(6)
        x_bango=str(i+1).zfill(6)
        bango_list[d[key][i][2]]=p_bango+x_bango

for b in bango_list:
    print(b)
