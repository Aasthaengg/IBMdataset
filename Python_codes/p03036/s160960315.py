r,d,x = (int(x) for x in input().split())

arr = [0] * 11
arr[0] = x 
for x in range(0,10):
    arr[x+1] = r * arr[x] - d
    print(arr[x+1])