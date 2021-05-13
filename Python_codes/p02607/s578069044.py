N = int(input())
arr = list(map(int, input().split()))
count = sum([ 1 for x in arr[::2] if x % 2 == 1])
print(count)