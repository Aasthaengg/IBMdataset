K,A,B=map(int,input().split())
s=B-A
if s<=2:
    print(K+1)
else:
    K-=A-1
    print(A+s*(K//2)+K%2)