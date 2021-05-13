a,b,c = map(int,input().split())
arr = [a,b,c]
arr.sort()
list.sort(arr, reverse=True)
tmp = abs(arr[0] - arr[1])
tmp += abs(arr[1] - arr[2])
print(tmp)