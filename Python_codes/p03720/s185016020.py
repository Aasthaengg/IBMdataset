from collections import Counter
N, M = map(int, input().split())
dis_list = []
my_count = Counter()
for i in range(1, N + 1):
    my_count[i] = 0
for i in range(M):
    a, b = map(int, input().split())
    my_count[a] += 1
    my_count[b] += 1
my_count = sorted(my_count.items())
for i in range(N):
    print(my_count[i][1])