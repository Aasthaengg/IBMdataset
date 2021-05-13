n=int(input())
i=0
while not 2**i<=n<2**(i+1):
    i+=1
print(2**i)
    
