n,m = map(int, input().split())
c = []
d = [0 for i in range(m+1)]
for i in range(n):
    arr = input().split()
    sum = 0
    for j in range(m):
        sum += int(arr[j])
        d[j] += int(arr[j])
    arr.append(sum)
    d[m] += sum
    c.append(arr)
c.append(d)
for i in range(n+1):
    print(" ".join(map(str,c[i])))