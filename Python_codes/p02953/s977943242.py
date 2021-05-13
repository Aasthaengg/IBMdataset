n = int(input())
h = list(map(int, input().split()))
for i in range(n):
    if i == 0 or h[i - 1] < h[i]:
        h[i] -= 1
for i in range(n - 1):
    if h[i] > h[i + 1]:
        print('No')
        break
else:
    print('Yes')
