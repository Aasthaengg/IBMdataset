N,K,Q=map(int,input().split())
arr=[K-Q]*N

for i in range(Q):
    a=int(input())
    arr[a-1]+=1

for i in arr:
    if i>0:
        print("Yes")
    else:
        print("No")
