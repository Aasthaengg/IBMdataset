N = int(input())
a = list(map(int, input().split()))

cnt = 0

for i in range(N):
    if i+1 != a[i] and i+1 == a[a[i]-1]:
        a[a[i]-1] = 0
        a[i] = 0

print(a.count(0) // 2)