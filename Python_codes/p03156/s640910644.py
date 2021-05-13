import numpy as np

N = int(input())

A, B = [int(i) for i in input().split()]

P = [int(i) for i in input().split()]



def Three_Categorize(P,A,B):
    count_1 = 0
    count_2 = 0
    count_3 = 0
    for i in P:
        if i <= A:
            count_1 +=1
        elif (i > A) & (i <= B):
            count_2 +=1
        elif i > B:
            count_3 +=1
    
    return [count_1, count_2, count_3]
            
    
count = Three_Categorize(P,A,B)
ans=min(count)
print(ans)
