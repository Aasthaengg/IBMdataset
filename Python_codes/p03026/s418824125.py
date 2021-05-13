n = int(input())
edge = [ [ int(v)-1 for v in input().split() ] for i in range(n-1) ]
num_list = sorted([ int(v) for v in input().split() ])
parent_list = [ None for i in range(n) ]
connect_list = [ [] for i in range(n) ]

for a, b in edge:
    connect_list[a].append(b)
    connect_list[b].append(a)

connect_point = [ len(i) for i in connect_list ]
p = connect_point.index(max(connect_point))

depth_list = [[p]]
search_list = [p]
parent_list[p] = -1

while search_list:
    new_search_list = []
    for i in search_list:
        for j in connect_list[i]:
            if parent_list[j] is None:
                parent_list[j] = i
                new_search_list.append(j)
    if new_search_list:
        depth_list.append(new_search_list)
    search_list = new_search_list

node = [ None for i in range(n) ]
q = 0

for i in depth_list[::-1]:
    for j in i:
        node[j] = num_list[q]
        q += 1

print(sum(num_list[:-1]))
print(*node)