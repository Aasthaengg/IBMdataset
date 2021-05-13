a,b,c=map(int,input().split())

A=[a]+[0]*10**5
B=[b]+[0]*10**5
C=[c]+[0]*10**5

i=0
while A[i]%2+B[i]%2+C[i]%2==0:
    i+=1
    A[i]=B[i-1]//2+C[i-1]//2
    B[i]=C[i-1]//2+A[i-1]//2
    C[i]=A[i-1]//2+B[i-1]//2
    if A[i]==B[i]==C[i]:
        i=-1
        break
print(i)