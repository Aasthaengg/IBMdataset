n = int(input())
a = list(map(int, input().split()))

input_num = [0 for _ in range(n)]

for i in range(n-1, -1, -1):
    tmp = 0
    j = i+i+1
    while j < n:
        tmp += input_num[j]
        j += i+1

    if tmp % 2 != a[i]:
        input_num[i] = 1

print(sum((input_num)))
for i, j in enumerate(input_num):
    if j:
        print(i+1, end=' ')