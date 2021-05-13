n = int(input())
arr = [int(a) for a in input().split()]

i = max(arr)
arr.remove(i)
j = min(arr, key=lambda a: abs(i/2-a))

print(i, j)
