n = int(raw_input())
arr = map(int, raw_input().split(' '))

p = 1
print ' '.join(map(str, arr))
while True:
    if p >= len(arr):
        break
    for j in range(0,p):
        if arr[p] < arr[j]:
            arr[p],arr[j] = arr[j],arr[p]
    p += 1
    print ' '.join(map(str, arr))