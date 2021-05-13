n = int(input())
a = [int(i) for i in input().split()]
avg = sum(a) / n
dis = max(a)
index = 0
for i in range(n):
    tmp = abs(a[i] - avg)
    if tmp < dis:
        index = i
        dis = tmp
print(index)