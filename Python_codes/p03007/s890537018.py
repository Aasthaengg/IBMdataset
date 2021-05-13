N = int(input())

A_list = list(map(int, input().split()))

A_sorted = sorted(A_list)

pos_count = len([a for a in A_sorted if a >= 0])
neg_count = len([a for a in A_sorted if a < 0])

if pos_count == 0:
    pos_count = 1
    neg_count = N - 1
if neg_count == 0:
    pos_count = N - 1
    neg_count = 1

output_list = [0] * (N - 1)
count = 0
for q in range(neg_count, N - 1):
    output_list[count] = [A_sorted[0], A_sorted[q]]
    count += 1
    A_sorted[0] -= A_sorted[q]


for i in range(neg_count):
    output_list[count] = [A_sorted[N - 1], A_sorted[i]]
    count += 1
    A_sorted[N - 1] -= A_sorted[i]

print(A_sorted[N - 1])
for item in output_list:
    print(item[0], item[1])