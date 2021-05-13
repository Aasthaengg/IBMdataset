def tc(arr):
    tn = arr[0]/arr[2]
    return "Yes" if tn<=arr[1] else "No"





u = list(map(int, input().split()))
print(tc(u))
