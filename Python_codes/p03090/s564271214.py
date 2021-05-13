#n=input()
#li=input().split()
#d=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#import math
#li=list(map(int,input().split()))

n=int(input())
if n%2==0:
    ans=int((n**2)/2)-n
    print(ans)
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if i+j!=n+1:
                print(i,j)

else:
    ans=int(((n-1)**2)/2)
    print(ans)
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if i+j!=n:
                print(i,j)
