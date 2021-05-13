n=int(input())

big = 10**6+10

furui = [0]*big
furui[0]=1
furui[1]=1

for i in range(2,big):
    if furui[i]==0:
        for j in range(i,len(furui),i):
            furui[j] = 1
            furui[i]=0
        
prime = [i for i in range(len(furui)) if furui[i]==0]

soinsuu=[]
for p in prime:

    while n%p==0:
        n //= p
        soinsuu.append(p)

if n!=1:
    soinsuu.append(n)
    
# print(soinsuu)

ans=0

for i in set(soinsuu):
    
    kai = ((8*soinsuu.count(i)+1)**0.5 -1)/2
    ans += int(kai)
    
print(ans)    
