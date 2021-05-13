D,G=list(map(int,input().split()))
pc = [[int(i) for i in input().split()] for m in range(D)]

#print(pc)
minn=10000
flug=[]
def func(D,G,pc,flug,i=0,summ=0,num=0):
    global minn
    if i==D:
        #print(flug,summ,num)
        if summ>=G:
            minn=min(minn,num)
            return 0
        else:
            for j,bit in enumerate(reversed(flug)):
                if bit==0:
                    for k in range(pc[D-1-j][0]):
                        summ+=(D-j)*100
                        num+=1
                        if summ>=G:
                            minn=min(minn,num)
        return 0

    return func(D,G,pc,flug+[1],i+1,summ+pc[i][0]*100*(i+1)+pc[i][1],num+pc[i][0]) + func(D,G,pc,flug+[0],i+1,summ,num)


func(D,G,pc,flug)
print(minn)