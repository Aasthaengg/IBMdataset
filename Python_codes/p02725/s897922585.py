k,n=[int(i) for i in input().strip().split(" ")]
arr=[int(i) for i in input().strip().split(" ")]
maxDist=arr[0]+min(k-arr[-1],arr[-1]) 
# maxDist=max(arr)-min(arr)
for i in range(n-1):
    maxDist=maxDist if arr[i+1]-arr[i] <=maxDist else arr[i+1]-arr[i]
print(k-maxDist)