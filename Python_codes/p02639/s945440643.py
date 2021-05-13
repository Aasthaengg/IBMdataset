arr = list(map(int, input().split()))
for idx, num in enumerate(arr):
    if num == 0:
        print(idx+1)
        break
    else:
        continue