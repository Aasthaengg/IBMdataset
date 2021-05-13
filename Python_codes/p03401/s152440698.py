n = int(input())
c = list(map(int,input().split()))
a = [0]
a += c
a.append(0)
b = [0 for i in range(n+1)]
b[0] = abs(a[1])
count = abs(a[1])
for i in range(1,n):
    b[i] = abs(a[i+1]-a[i])
    count += b[i]
count += abs(a[n])
b[n] = abs(a[n])
for i in range(n):
    print(count - b[i] - b[i+1] + abs(a[i+2] - a[i]))