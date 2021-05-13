import numpy as np

N=int(input())
count=[]
for n in range(1,N+1):
    count_n=0
    while n%2==0:
        n=n/2
        count_n+=1
    count.append(count_n)

answer=count.index(max(count))+1
print(answer)
