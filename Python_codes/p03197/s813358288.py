n = int(input())
arr = [int(input()) for _ in range(n)]
print("second"if all(arr[i] % 2 == 0 for i in range(n)) else "first")