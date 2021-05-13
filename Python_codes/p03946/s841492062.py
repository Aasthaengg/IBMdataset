N, T = map(int, input().split())
A = list(map(int, input().split()))

min_num = 10 ** 9 + 7
diff = 0
count = 0
for i in range(N):
    min_num = min(min_num, A[i])
    if diff == A[i] - min_num:
        count += 1
    elif A[i] - min_num > diff:
        count = 1
        diff = A[i] - min_num
    else:
        continue

print(count)
