n = int(input())
l = [0]*n
r = [0]*n
count = 0
for i in range(n):
    arr = input().split()
    arr = list(map(int,arr))
    l[i] = arr[0]
    r[i] = arr[1]
    count += r[i] - l[i] + 1
print(count)
