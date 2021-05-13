N=int(input())
for i in range(1,3501):
   for j in range(1,3501):
         a=N*i*j
         b=4*i*j-N*j-N*i
         if b>0:
            if (a/b).is_integer() == True:
               print(i,j,int((N*i*j)/(4*i*j-N*j-N*i)))
               exit()