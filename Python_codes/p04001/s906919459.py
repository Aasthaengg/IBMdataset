st_N=input()
N=int(st_N)


output=0
for i in range(1<<(len(st_N)-1)):
    f=st_N[0]
    for j in range(len(st_N)-1):

        if((i>>j) & 1)==1:
            f=f+'+'
        f=f+st_N[j+1]
    #print(f)
    output=output+sum(map(int,f.split('+')))

print(output)
