n = int(input())
A = sorted(map(int, input().split()), reverse = True)

x = 0; y = 0
count = 0
i = 0
while i < n - 1:
    if A[i] == A[i + 1]:
        if count == 0:
            x = A[i]
        else:
            y = A[i]
        count += 1
        i += 2
    else:
        i += 1
    if count == 2:
        break

print(x * y)
