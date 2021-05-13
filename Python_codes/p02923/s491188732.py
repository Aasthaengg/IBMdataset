N = int(input())
H = list(map(int, input().split()))
l = []
for i in range(N):
    if i == 0:
        l.append(0)
    elif H[i - 1] >= H[i]:
        l.append(l[i - 1] + 1)
    elif H[i - 1] < H[i]:
        l.append(0)
print(max(l))
