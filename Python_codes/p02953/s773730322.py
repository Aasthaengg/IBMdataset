n = int(input())
h = list(map(int, input().split()))
mi = h[-1]
for i in range(n - 2, -1, -1):
    if h[i] > mi + 1:
        print("No")
        exit()
    mi = min(mi, h[i])
print("Yes")