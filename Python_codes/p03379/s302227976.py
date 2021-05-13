import numpy as np
n=int(input())
l=list(map(int,input().split()))

arr=np.sort(np.array(l))
med=np.median(arr)

med_max=int(np.median(np.delete(arr,0)))
med_min=int(np.median(np.delete(arr,n-1)))

if n%2==1:
    p=(n-1)//2
    med_midmin=int(np.median(np.delete(arr,p+1)))
    med_mid=int(np.median(np.delete(arr,p)))
    med_midmax=int(np.median(np.delete(arr,p-1)))

    for i in range(n):
        if l[i]<arr[p-1]:
            print(med_max)
        elif l[i]==arr[p-1]:
            print(med_midmax)
        elif l[i]==arr[p]:
            print(med_mid)
        elif l[i]==arr[p+1]:
            print(med_midmin)
        else:
            print(med_min)

if n%2==0:
    p=(n+1)//2
    med_midmin=int(np.median(np.delete(arr,p)))
    med_midmax=int(np.median(np.delete(arr,p-1)))
    for i in range(n):
        if l[i]<arr[p-1]:
            print(med_max)
        elif l[i]==arr[p-1]:
            print(med_midmax)
        elif l[i]==arr[p]:
            print(med_midmin)
        else:
            print(med_min)