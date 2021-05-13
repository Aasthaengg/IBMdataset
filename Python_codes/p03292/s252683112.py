a, b, c= map(int, input().split())
arr = [abs(a - b), abs(b - c), abs(c - a)]
arr.sort()
print(arr[0] + arr[1])