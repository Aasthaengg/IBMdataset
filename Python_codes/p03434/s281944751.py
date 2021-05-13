
N,*list1 = open(0).read().split()

N=int(N)

#print(N)

list1=[int(i) for i in list1]

list1.sort(reverse=True)

#print(list1)

aaa=[]

bbb=[]


for i,n in enumerate(list1):
    if (i+1)%2 == 1:
        aaa.append(list1[i])
    else:
        bbb.append(list1[i])


#print(aaa)

#print(bbb)

print(sum(aaa)-sum(bbb))