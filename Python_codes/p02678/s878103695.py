inlist=input("").split(" ")
n=int(inlist[0])
m=int(inlist[1])
lista=[]
listb=[]
for i in range(n):
    lista+=[[]]
    listb+=[-1]
listb[0]=-2

listnum=[0]
for i in range(m):
    inlist=input("").split(" ")
    s=int(inlist[0])
    t=int(inlist[1])
    lista[s-1]+=[t-1]
    lista[t-1]+=[s-1]
k=0
while(k<len(listnum)):
    for i in lista[listnum[k]]:
        
        if(listb[i]==-1):
            listb[i]=listnum[k]
            listnum+=[i]
    k+=1

if (-1 in listb):
    print("No")
else:
    print("Yes")
    for i in listb[1:]:
        print(i+1)
        
    






    
    
    

    
    
