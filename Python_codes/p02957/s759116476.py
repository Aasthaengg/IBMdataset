arr = list(map(int, input().split()))

a, b = arr[0], arr[1]

if (a+b)%2 == 0: print(int((a+b)/2))
else: print("IMPOSSIBLE")