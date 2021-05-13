K,A,B=map(int,input().split())

if A+2>=B or K-1<A:
    print(1+K)
else:
    if (K-A+1)%2==0:
        print(A+((K-A+1)//2)*(B-A))
    else:
        print(A+((K-A+1)//2)*(B-A)+1)
