N = int(input())
a = list(map(int, input().split()))
count = 0
for i in range(0, N-1):
    if a[i+1] < a[i]:
        count += a[i]-a[i+1]
        a[i+1] = a[i]
print(count)