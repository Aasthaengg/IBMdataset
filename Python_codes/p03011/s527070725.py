arr = input().split()
p,q,r=int(arr[0]),int(arr[1]),int(arr[2])
print(min(p+q,p+r,q+r))