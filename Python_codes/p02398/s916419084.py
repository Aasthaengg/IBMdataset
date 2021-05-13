[a,b,c]=[int(x) for x in input().split()]
counter=0
for i in range(a,b+1):
    if c%i==0:
        counter=counter+1
print(counter)