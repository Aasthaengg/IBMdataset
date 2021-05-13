n = int(input())
h = list(map(int, input().split()))
for i in range(1, n):
    if h[i] >= h[i - 1] + 1:
        h[i] = h[i] - 1
    elif h[i] < h[i - 1]:
        print('No')
        exit()
print('Yes')
