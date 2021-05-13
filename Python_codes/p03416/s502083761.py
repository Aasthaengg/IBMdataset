a,b=[int(i) for i in input().split()]

count=0   
for i in range(a,b+1):
    if str(i)==str(i)[::-1]:
        
        count+=1
        
print(count)