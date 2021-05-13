K, N = map(int, input().split())
A = list(map(int, input().split()))

diff_list = []
for i in range(N - 1):
    current = A[i]
    next = A[i + 1]
    diff_list.append(next - current)

diff_list.append(K - A[-1] + A[0])

max_index = diff_list.index(max(diff_list))
del diff_list[max_index]

print(sum(diff_list))
