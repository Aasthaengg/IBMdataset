n = int(input())
p = list(map(int, input().split()))
num = 0
for i in range(1, n - 1):
    if p[i] > p[i - 1] and p[i] < p[i + 1]:
        num += 1
    elif p[i] < p[i - 1] and p[i] > p[i + 1]:
        num += 1
    else:
        continue
print(num)