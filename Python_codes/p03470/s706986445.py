import math
N=int(input())
array = [0]*N
for i in range(N):
    array[i]=int(input())
array=sorted(array)
max=array[N-1]+1
bucket=[0]*(max+1)
for val in array:
    bucket[val]=bucket[val]+1
s=0
for i in range(max+1):
    if bucket[i]>0:
        s=s+1
print(s)
