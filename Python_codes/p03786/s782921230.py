n = int(input())
l = sorted(list(map(int, input().split())))
idx = 0
cum = 0
for i in range(n-1):
    cum += l[i]
    if cum*2 < l[i+1]:
        idx = i+1
print(n-idx)

