h,w,n=map(int,input().split())
ls=[]
while True:
    try:
        ls.append(tuple(map(int,input().split())))
    except EOFError:break
check={}
count={0:(h-2)*(w-2)}
for i in range(1,10):
    count[i]=0
for tup in ls:
    for i in range(-2,1):
        for j in range(-2,1):
            if(tup[0]+i>0 and tup[0]+i<h-1 and tup[1]+j>0 and tup[1]+j<w-1):
              try:
                check[(tup[0]+i,tup[1]+j)]+=1
              except KeyError:
                check[(tup[0]+i,tup[1]+j)]=1
              index=check[(tup[0]+i,tup[1]+j)]
              count[index]+=1
              count[index-1]-=1
for i in range(10):
    print("{}".format(count[i]))