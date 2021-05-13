from itertools import combinations_with_replacement

N, M, Q = list(map(int, input().split()))
num_list = [list(map(int, input().split())) for _ in range(Q)]

m_range = list(range(1, M+1))
max_point = 0
for array in combinations_with_replacement(m_range, N):
    point = 0
    for (a, b, c, d) in num_list:
        if array[b-1] - array[a-1] == c:
            point += d
    max_point = max(max_point, point)
print(max_point)