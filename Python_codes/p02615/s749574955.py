n = int(input())
arr = [int(x) for x in input().split()]
arr = sorted(arr)
arr.reverse()
d = []
d.append(1)
current = 0
s = 0
for i in range(1,len(arr)):
    d[current] -= 1
    s += arr[current]
    if d[current] == 0:
        current += 1
    d.append(2)
print(s)
