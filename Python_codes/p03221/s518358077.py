n,m=map(int,input().split())
citydic={}
for i in range(m):
    p,y=map(int,input().split())
    add=[i,p,y]
    temp=citydic.get(p,[])
    temp.append(add)
    citydic[p]=temp

#print(citydic)
def make_id(p):
    dif=6-len(str(p))
    res="".join(["0" for i in range(dif)])
    return res+str(p)

ansdic={}
for key, v in citydic.items():
    l=sorted(v,key=lambda x: x[2])
    #print(l)
    for x, templ in enumerate(l,1):
        #makeid
        citynum,p,y=templ
        id1=make_id(p)+make_id(x)
        ansdic[citynum]=id1

for i in range(m):
    print(ansdic[i])
