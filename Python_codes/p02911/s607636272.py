inp=list(map(int,input().split()))
n=inp[0]
k=inp[1]
q=inp[2]
arr=[k-q]*n
for i in range(q):
        x=int(input())
        arr[x-1]+=1
if q<k:
    for i in range(n):
        print ('Yes')
else:
    z=[]
    for i in range(len(arr)):
        if arr[i]>0:
            print ('Yes')
        else:
            print ('No')