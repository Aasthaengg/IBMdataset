N, M = list(map(int, input().split(' ')))
left_list = list()
right_list = list()
for _ in range(M):
    a, b = list(map(int, input().split(' ')))
    left_list.append(a)
    right_list.append(b)
sorted_blocking_section_list = sorted(range(M), key=lambda i: right_list[i])
blocking_bridge = None
blocking_bridge_cnt = 0
for section in sorted_blocking_section_list:
    left_bridge = left_list[section]
    right_bridge = right_list[section] - 1
    if blocking_bridge is None or blocking_bridge < left_bridge:
        blocking_bridge = right_bridge
        blocking_bridge_cnt += 1
print(blocking_bridge_cnt)