n = int(input())
h = list(map(int, input().split()))
h = h[::-1]

for i in range(1, n):
    dh = h[i] - h[i - 1]
    if dh == 1:
        h[i] -= 1
    elif dh > 1:
        print('No')
        exit()

print('Yes')     