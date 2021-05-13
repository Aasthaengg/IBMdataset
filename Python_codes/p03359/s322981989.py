a,b=map(int,input().split())
ct=0
for i in range(1,a+1):
    for j in range(1,32):
        if(a!=b):
            if(i==b):
                break
            elif(i==j):
                ct=ct+1
        elif(i==j):
            ct=ct+1
               
print(ct)
