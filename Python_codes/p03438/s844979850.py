(n,),a,b=[[*map(int, i.split())]for i in open(0)]
print("YNeos"[sum(j - i if i > j else (j-i)//2 for i, j in zip(a,b))<0::2])
