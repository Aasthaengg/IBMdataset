# coding: utf-8
# Your code here!
K,A,B=map(int,input().split())

if B-A>2:
    if K<=A:
        print(K+1)
    else:
        K-=A-1
        
        print((B-A)*(K//2)+A+K%2)
    
    
else:
    print(K+1)
