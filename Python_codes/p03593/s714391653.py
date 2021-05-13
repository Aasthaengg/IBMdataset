import collections

h,w=map(int, input().split())
a=[list(input()) for i in range(h)]
x=[]

for i in range(h):
    x+=a[i]

c = collections.Counter(x)
c = c.most_common()


if h%2==0 and w%2==0:
    for i in range(len(c)):
        if c[i][1]%4!=0:
            print('No')
            exit()

elif h%2==1 and w%2==0:
    for i in range(len(c)):
        if c[i][1]%4==0:
            continue
        elif c[i][1]%4==2:
            w-=2
            if w<0:
                print('No')
                exit()
        else:
            print('No')
            exit()
    

elif h%2==0 and w%2==1:
    for i in range(len(c)):
        if c[i][1]%4==0:
            continue
        
        elif c[i][1]%4==2:
            h-=2
            if h<0:
                print('No')
                exit()
        else:
            print('No')
            exit()

else:
    v=h+w-2
    r=1
    for i in range(len(c)):
        if c[i][1]%4==0:
            continue
        
        elif c[i][1]%4==3:
            v-=2
            r-=1
            if v<0 or r<0:
                print('No')
                exit()
                
        elif c[i][1]%4==2:
            v-=2
            if v<0:
                print('No')
                exit()
        
        else:
            r-=1
            if r<0:
                print('No')
                exit()
print('Yes')
            


        


                    
                    
                    

    




    
    
        

