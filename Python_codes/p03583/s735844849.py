n=int(input())
for i in range(3500):
    for j in range(3500):
        if 4*i*j-n*(i+j)>0 and n*i*j%(4*i*j-n*(i+j))==0:
            print(i,j,n*i*j//(4*i*j-n*(i+j)))
            exit()