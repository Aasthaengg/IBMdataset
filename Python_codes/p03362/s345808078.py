import math

n=int(input())

def prime_check(x): #x>=2
    if x==2:
        return True
    elif x%2==0:
        return False
    else:
        limit=int(math.sqrt(x))
        for factor in range(3,limit+1,2):
            if x%factor==0:
                return False
        return True

temp=11
count=0
L=[]
while True:
    if prime_check(temp):
        L.append(temp)
        count+=1
    
    if count==n:
        break
    else:
        temp+=10

print(*L)



