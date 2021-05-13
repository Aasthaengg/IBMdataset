n = int(input())
A = list(map(int, input().split()))
prev = -1
count = 0
total = 0
for i in range(n):
    if prev == A[i]:
        count += 1
    else:
        total += (count + 1) // 2
        count = 0
    prev = A[i]
total += (count + 1) // 2
print(total)