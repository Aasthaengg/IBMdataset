(n,),a,b=[[*map(int,i.split())]for i in open(0)]
print("YNeos"[sum(min(j-i,(j-i)//2) for i,j in zip(a,b))<0::2])
