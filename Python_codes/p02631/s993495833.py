n = int(input())
a = list(map(int, input().split()))

count = 0
for k in a:
    count ^= k


for i in range(n):
    count ^= a[i]
    print(count, end=' ')
    count ^= a[i]
print()


