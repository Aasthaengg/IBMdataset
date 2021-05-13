K,A,B=map(int,input().split())

if (B-A)/2>1 and K>=A+1:
    print(A+(B-A)*((K-A+1)//2)+(K-A+1)%2)
else:
    print(K+1)