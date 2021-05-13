N = int(input())
H = list(map(int, input().split()))
num, max = 0, 0
for i in range(N - 1):
    if H[i] >= H[i + 1]:
        num += 1
    else:
        if num > max:
            max = num
        num = 0
if num > max:
        max = num
print(max)