Num = int(input())
a = list(map(int, input().split()))
k = 0
for i in range(1, Num):
    if a[i-1] == a[i]:
        a[i] = 0
        k += 1
print(k)