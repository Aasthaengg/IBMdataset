n, k = map(int, input().split())
a = list(map(int, input().split()))

count = [0] * n

for x in range(n):
    count[a[x]-1] += 1

count.sort()
length = len(count)

print(sum(count[:length - k]))
