a,b,k=map(int,input().split())

if b-a>200:
    for i in range(k):
        print(a+i)
    for i in range(k):
        print(b-k+1+i)
    
else:
    arr=[]
    for i in range(a,b+1):
        if i<a+k or i>b-k:
            arr.append(i)
    for i in range(len(arr)):
        print(arr[i])