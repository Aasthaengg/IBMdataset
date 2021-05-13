N,Y = list(map(int,input().split()))

a=-1
b=-1
c=-1
for i in range(0,N+1):
    for j in range(0,N-i+1):
        if 10000*i+5000*j+1000*(N-i-j)==Y:
            a=i
            b=j
            c=N-i-j
            break
                            
print(a,b,c)