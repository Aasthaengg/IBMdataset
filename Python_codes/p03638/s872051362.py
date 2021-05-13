h,w=map(int,input().split())
n=int(input())
a=list(map(int,input().split()))
lis=[]
count=0
for i in a:
    count+=1
    for j in range(i):
        lis.append(count)
for i in range(h):
    for j in range(w):
        if i%2==0:
            print(lis[i*w+j],end=" ")
        else:
            print(lis[(i+1)*w-1-j],end=" ")
    print()