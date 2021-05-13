from collections import defaultdict

N, W = map(int, input().split())

data_list = []
for i in range(N):
    w, v = map(int, input().split())
    data_list.append((w, v))
    
data = defaultdict(int)
data[0] = 0
for w, v in data_list:
    for cw, cv in list(data.items()):
        if cw + w <= W:
            data[cw+w] = max(data[cw+w], cv+v)
            
print(max(data.values()))