data = list(map(int,input().split()))
n = data[0]
k = data[1]
del data
if k > 1:
    if n >= k:
        print(n-k)
    elif n < k:
        print("1")
else:
    print(0)