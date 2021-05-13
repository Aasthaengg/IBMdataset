n = int(input())
a = input().split()
b = a[:]
flag = 1
while flag:
    flag = 0
    for i in range(n-1):
        if a[i][1] > a[i+1][1]:
            a[i], a[i+1] = a[i+1], a[i]
            flag = 1
print(*a)
print("Stable")

for i in range(n-1):
    min_j = i
    for j in range(i,n):
        if b[j][1] < b[min_j][1]:
            min_j = j
    b[i], b[min_j] = b[min_j], b[i]
print(*b)
if a == b:
    print("Stable")
else:
    print("Not stable")