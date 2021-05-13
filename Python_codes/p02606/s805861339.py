# cook your dish here
lrd=list(map(int , input().split()))
l=lrd[0]
r=lrd[1]
d=lrd[2]
count=0
for i in range(l,r+1):
    if(i%d==0):
        count+=1
        
        
    
print(count)