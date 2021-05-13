N,K=map(int,input().split())
count=0
num=N//K
count+= num + num*(num-1)*(num-2) + num*(num-1)*3
if K%2==0:
    K=K//2
    num=(N//K)//2+1*((N//K)%2==1)

    count+= num + num*(num-1)*(num-2) + num*(num-1)*3
print(count)
