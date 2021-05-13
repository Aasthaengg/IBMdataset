N, K = map(int, input().split())

data_dict = {}

for k in range(K):
    data_dict[k] = 0

for n in range(N):
    if n in data_dict:
        if data_dict[n] == 0:
            data_dict[n] = 1
    else:
        data_dict[0] += 1

print(data_dict[0] - data_dict[K - 1])