def inp():
    return(int(input()))


def invr():
    return(map(int, input().split()))


n = inp()
arr = invr()
arr = sorted(arr)
d = 0
for i in range(n-1):
    d += arr[i+1] - arr[i]
print(d)
