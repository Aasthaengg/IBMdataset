n = int(input())
h = list(map(int, input().split()))
h = h[::-1]

for i in range(1,n):
    if h[i] > h[i-1]:
        h[i] -= 1
        if h[i] < 1 or h[i] > h[i-1]:
            print('No')
            exit()
print('Yes')