n = int(input())
h = list(map(int, input().split()))
max_ = h[0]

for i in range(1, n - 1):
    max_ = max(max_, h[i])
    if max_ - h[i + 1] >= 2:
        print("No")
        exit()
print("Yes")