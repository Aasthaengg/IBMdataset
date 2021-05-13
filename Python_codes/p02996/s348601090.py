n = int(input())
a = [0] * n
b = [0] * n
arr = [[0] * 2 for _ in range(n)]

for i in range(n):
    a[i], b[i] = map(int, input().split())
    arr[i][0] = b[i]
    arr[i][1] = a[i]

arr.sort()
time = 0
flag = True
for i in range(n):
    time += arr[i][1]
    if time > arr[i][0]:
        flag = False
if flag:
    print('Yes')
else:
    print('No')

