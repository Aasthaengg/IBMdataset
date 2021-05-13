n = int(input())
L=[]
st=0
sh=0
for i in range(n):
    x,y=input().split()
    L.append([x,y])




for i in L:
    j=sorted(i)
    if i[0] == i[1]:
        st+=1
        sh+=1
    else:
        if i[0] ==j[0]:
            sh += 3
        else:
            st+=3


print (st,sh)