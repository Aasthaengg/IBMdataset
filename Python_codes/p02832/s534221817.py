n = int(input())
a = list(map(int, input().split()))

if not 1 in a:
    print(-1)
    exit()

k = 1
for i in range(n):
    if a[i] == k:
        k += 1
print(n-k+1)