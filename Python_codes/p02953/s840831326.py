n=int(input())
h=list(map(int,input().split()))
num=h[0]
for i in range(1,n):
    if h[i]<num:
        print("No")
        exit()
    else:
        if h[i]>num:
            num=h[i]-1
print("Yes")