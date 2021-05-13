n=int(input())
arr=[int(i) for i in input().split()]
so_far=arr[0]
tot=0
for i in range(1,n):
    if arr[i]<so_far:
        tot+=so_far-arr[i]
    else:
        so_far=arr[i]
print(tot)