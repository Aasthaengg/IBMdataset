# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))


res = 0
i=0

while(i<N):    
    #same
    while(i+1 < N and A[i] == A[i+1]):
        i+=1
    
    #up
    if(i+1 < N and A[i] < A[i+1]):
        while(i+1 < N and A[i] <= A[i+1]):
            i+=1
    
    #down
    elif(i+1 < N and A[i] > A[i+1]):
        while(i+1 < N and A[i] >= A[i+1]):
            i+=1

    res+=1
    i+=1
   


print(res)
