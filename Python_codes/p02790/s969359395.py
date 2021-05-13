a, b = list(map(int, input().split()))
arr = [str(a) * b, str(b) * a]
arr.sort()
print(arr[0])