N = int(input())
B = list(map(int, input().split()))

tot_sum = 2 * B[0]
prev = B[0]
for i in range(1, N - 1):
    if prev >= B[i]:
        tot_sum -= prev
        tot_sum += 2 * B[i]
    else:
        tot_sum += B[i]
    prev = B[i]
print(tot_sum)