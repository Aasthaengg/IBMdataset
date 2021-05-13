n=int(input())
a=sorted(list(map(int,input().split())),reverse=True)

i=0
arr=[]
while i<n-1:
    if a[i]==a[i+1]:
        arr.append(a[i])
        i+=2
    else:
        i+=1
    if len(arr)==2:
        print(arr[0]*arr[1])
        exit()
print(0)