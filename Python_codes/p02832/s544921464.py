n = int(input())
a = list(map(int, input().split()))

count = 0
target = 1

if not (1 in a):
    print(-1)
    exit()

for i in range(n):
    if a[i] == target:
        target += 1
    else:
        count += 1

print(count)
