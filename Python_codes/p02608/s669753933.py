n = int(input())
li = [0]*10050

for i in range(1,105):
    for j in range(1,105):
        for k in range(1,105):
            s = i*i+j*j+k*k+i*j+j*k+i*k
            
            if s<10050:
                li[s]+=1
                
for i in range(1,n+1):
    print(li[i])