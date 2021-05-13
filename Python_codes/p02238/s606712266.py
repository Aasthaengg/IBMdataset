class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = list()
        self.find_time = 0
        self.end_time = 0

N = int(input())
work_id = 0
nodes = list()
nodes.append(Node(0))


for _ in range(N):
    tmp_list = list( map(int, input().split()) )
    node = Node(tmp_list[0])
    for i in range(tmp_list[1]):
        node.neighbors.append(tmp_list[i+2])
    nodes.append(node)
    nodes[0].neighbors.append(node.data)

# for node in nodes:
#     print(node.data, ":", node.neighbors)


def search(node):
    global work_id

    if node.find_time != 0:
        return
    
    if node.data != 0:
        work_id += 1
        node.find_time = work_id

    if len(node.neighbors) > 0:
        for neighbor in node.neighbors:
            search(nodes[neighbor])
    
    if node.data != 0:
        work_id += 1
        node.end_time = work_id

search(nodes[0])

for node in nodes:
    if node.data == 0: continue
    print(node.data, node.find_time, node.end_time)

