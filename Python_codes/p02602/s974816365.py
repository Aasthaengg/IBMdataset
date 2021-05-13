n,k=map(int,input().split())
a=list(map(int,input().split()))
[print("Yes" if a[k+i]>a[i] else "No") for i in range(n-k)]