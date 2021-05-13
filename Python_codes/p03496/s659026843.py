# D
n = int(input())
ali = list(map(int, input().split()))

log = []
max_ = max(ali)
min_ = min(ali)

if abs(max_) >= abs(min_):
    max_index = ali.index(max_)+1
    for i in range(n):
        log_i = i+1
        log.append((max_index, log_i))
    for j in range(n-1):
        log_j = j+1
        mae = log_j
        ushiro = log_j+1
        log.append((mae, ushiro))
elif abs(max_) < abs(min_):
    min_index = ali.index(min_) + 1
    for i in range(n):
        log_i = i + 1
        log.append((min_index, log_i))
    for j in range(1, n)[::-1]:
        log_j = j+1
        mae = log_j
        ushiro = log_j -1
        log.append((mae, ushiro))

print(len(log))
for v1, v2 in log:
    print(str(v1) + ' ' + str(v2))