n=int(input(""))
lista=input("").split(" ")
lisa=[]
listn=[]
for i in range(n+1):
    listn+=[0]
for i in lista:
    lisa+=[int(i)]
    listn[int(i)]+=1
s=0
for i in listn:
    if(i<2):
        continue
    else:
        s+=i*(i-1)/2
for i in lisa:
    print(int(s-listn[i]+1))
    
    

    
    
    
    
