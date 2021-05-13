n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

p = a[0]
t = 0
for i in range(n):
    j = a[i]
    if a[i] == p + 1:
        t = t + b[j-1] + c[j-2]
    else:
        t += b[j-1]
    p = a[i]

print(t)