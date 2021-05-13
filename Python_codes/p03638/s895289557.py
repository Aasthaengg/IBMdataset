h,w=map(int,input().split())
n=int(input())
a=[int(i) for i in input().split()]
hw=[[0 for i in range(w)] for j in range(h)]

k=0
for i in range(h):
    if i%2==0:
        for j in range(w):
            if a[k]!=0:
                hw[i][j]=k+1
                a[k]-=1
            else:
                k+=1
                hw[i][j]=k+1
                a[k]-=1
    else:
        for j in range(w-1,-1,-1):
            if a[k]!=0:
                hw[i][j]=k+1
                a[k]-=1
            else:
                k+=1
                hw[i][j]=k+1
                a[k]-=1
for i in range(h):
    for j in range(w):
        if j==w-1:
            print(hw[i][j])
        else:
            print(hw[i][j],end=" ")
