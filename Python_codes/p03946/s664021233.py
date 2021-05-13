n, t = map(int, input().split())
A = list(map(int, input().split()))

min_dif = 0
count = 0
min_val = A[0]

for i in range(1, n):
    if A[i]-min_val > min_dif:
        min_dif = A[i]-min_val
        count = 1
    elif A[i]-min_val == min_dif:
        count += 1

    min_val = min(min_val, A[i])

print(count)
