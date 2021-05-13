n,m=map(int,input().split())
pyn=[]
for i in range(m):
    py=list(map(int,input().split()))
    py.append(i)
    pyn.append(py)

new_pyn=sorted(pyn)

cnt=1
i=1
j=0


while(j<m):
    if new_pyn[j][0] == i:
        new_pyn[j].append(cnt)
        cnt+=1
        j+=1

    else:
        cnt=1
        i+=1
final=sorted(new_pyn,key=lambda x:x[2])


for i in range(m):
    a=str(final[i][0])
    b=str(final[i][3])
    print(str(a.zfill(6))+str(b.zfill(6)))