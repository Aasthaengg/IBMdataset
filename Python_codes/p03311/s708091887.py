n = int(input())
a = list(map(int, input().split()))
a1 = []
for i in range(n):
    a1.append(a[i]-i-1)
a1.sort()
b = a1[n//2]
y = 0
for i in a1:
    y += abs(i-b)
print(y)