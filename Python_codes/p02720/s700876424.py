L=[]

def make_lunlun(A):
    
    # print(A)
   
    if not 0<A<10**10 :
        return
    
    global L
    # print(A)
    
    L.append(A)
    
    if(A%10 != 9):
        make_lunlun(A*10 + (A%10)+1)

    
    if(A!=0):
        make_lunlun(A*10+(A%10))

    
    if(A%10 != 0):
        make_lunlun(A*10 +(A%10)- 1)

    
k=int(input())


for i in range(10):
    make_lunlun(i)
  
L=list(set(L))
L.sort()

print(L[k-1])