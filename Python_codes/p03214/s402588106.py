n = int(input())
a = [int(s) for s in input().split()]

average = sum(a) / n
for i in range(n):
    a[i] = abs(average - a[i])
print(a.index(min(a)))