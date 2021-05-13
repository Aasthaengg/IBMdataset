n = int(input())
l = list(map(int, input().split(" ")))

arr_arr = []

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            arr = sorted([l[i], l[j], l[k]])
            if (arr[0] + arr[1] > arr[2]) and ((arr[0] != arr[1])and(arr[1] != arr[2])):
                arr_arr.append(arr)

print(len(arr_arr))