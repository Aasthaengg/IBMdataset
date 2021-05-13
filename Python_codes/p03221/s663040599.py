#n=int(input())
n,m=map(int,input().split())
#hl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

citydic={}

def make_id(p):
    dif=6-len(str(p))
    res="".join(["0" for i in range(dif)])
    return res+str(p)

for i in range(1,m+1):
    p,y=map(int,input().split())
    templ=citydic.get(p,[])
    templ.append([i,p,y])
    citydic[p]=templ

#print(citydic)
id_dic={}

for pref, val in citydic.items():
    l=sorted(val,key=lambda x: x[2])
    for x,temp in enumerate(l,1):
        i,p,y=temp
        # make id
        cityid=make_id(p)+make_id(x)
        id_dic[i]=cityid

for i in range(1,m+1):
    print(id_dic[i])

