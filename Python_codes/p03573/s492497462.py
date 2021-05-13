arr = list(map(int, input().split()))
print(sum(arr)-sorted(arr)[1]*2)