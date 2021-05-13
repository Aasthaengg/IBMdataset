N = int(input())
lis = list(map(int, input().split()))

half = sum(lis)
left, right, dif = 0, half, half

for i in range(N):
    dif_before = dif
    left += lis[i]
    right = half - left
    dif = abs(right - left)
    if dif >= dif_before:
        break

print(dif_before)