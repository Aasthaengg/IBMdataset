N = int(input())
A = sorted(map(int, input().split()))
sum_A = sum(A)
count = N
for i in range(N - 1, -1, -1):
    sum_A -= A[i]
    if (sum_A) * 2 >= A[i]:
        continue

    else:
        if (i == 0):
            continue
        count -= len(A[0:i])
        break

print(count)
