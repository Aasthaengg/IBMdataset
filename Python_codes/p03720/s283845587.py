n, m = map(int, input().split())
nodes = [input().split() for _ in range(m)]

node_num = {str(i): 0 for i in range(1, n + 1)}
for node in nodes:
    node_num[node[0]] += 1
    node_num[node[1]] += 1

for i in range(1, n + 1):
    print(node_num[str(i)])
