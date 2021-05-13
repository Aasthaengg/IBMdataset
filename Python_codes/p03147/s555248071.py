N = int(input())
arr = list(map(int, input().split()))
 
count =0
while True:
    if sum(arr) == 0:
        break
    count +=1
    start = False
 
    for i in range(N):
        if arr[i] != 0:
            arr[i] -= 1
            start = True
            continue
        if arr[i] == 0 and start == True:
            break
print(count)