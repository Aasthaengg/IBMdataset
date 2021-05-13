import copy

N = int(input())
org_arr = [list(input().split()) for _ in range(N)]
for i in range(len(org_arr)):
    org_arr[i][1]=int(org_arr[i][1])
    org_arr[i].append(i+1)

arr = copy.copy(org_arr)


arr = sorted(arr, reverse=True, key=lambda x: x[1])
arr.sort(key=lambda x:x[0])

for i in range(len(arr)):
    arr[i].append(i+1)

arr.sort(key=lambda x:x[0])
for i in range(len(arr)):
    print(arr[i][2])
