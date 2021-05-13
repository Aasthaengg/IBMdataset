r,D,x_2000=map(int,input().split())
glass=[x_2000]
for i in range(1,11):
    glass+=[r*glass[i-1]-D]
    print(glass[i])