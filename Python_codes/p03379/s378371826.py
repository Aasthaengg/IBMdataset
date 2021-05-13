import numpy as np
n=int(input())
l=list(map(int,input().split()))

arr=np.sort(np.array(l))
med=np.median(arr)

med_max=int(np.median(np.delete(arr,0)))
med_min=int(np.median(np.delete(arr,n-1)))


p=(n+1)//2
for i in range(n):
    if l[i]<=arr[p-1]:
        print(med_max)
    else:
        print(med_min)