N=int(input())
D={}
for i in range(2,int(N**0.5)+1):
    n=N
    #print(i,n)
    while n%i==0 and n!=i:
        n//=i
    #print(i,n)
    if n==i or n%i==1:
        D[i]=1
        #print("ANS",i,n)
#print(D)
N1=N-1
for i in range(1,int(N1**0.5)+1):
    if N1%i==0:
        D[i]=1
        D[N1//i]=1
#print(D)
print(len(D))
        
