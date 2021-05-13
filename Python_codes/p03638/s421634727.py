h,w=[int(i)for i in input().split()]
n=int(input())
a=[int(i)for i in input().split()]
arr=[]

count=0
for i in a:
    count+=1
    for j in range(i):
        arr.append(count)
        
for y in range(h):
    for x in range(w):
        if y%2==0:print(arr[y*w+x],end=" ")
        else:print(arr[(y+1)*w-1-x],end=" ")
    print("")