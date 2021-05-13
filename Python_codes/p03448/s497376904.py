x=int(input())
c=0
y,z,d=int(input()),int(input()),int(input())
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            f=500*i+100*j+50*k
            if(f==d):
                c+=1
print(c)
