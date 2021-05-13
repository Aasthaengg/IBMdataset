N = int(input())
arr = list(map(int, input().split()))

if sum(arr) == 0:
    print(0)
    exit()
#if N == 1:
#    print(arr[0])
#    exit()

count =0
while True:
    count +=1
    start = False

    for i in range(N):
        if arr[i] != 0:
            arr[i] -= 1
            start = True
            continue
        if arr[i] == 0 and start == True:
            break
    if sum(arr) == 0:
        break
print(count)