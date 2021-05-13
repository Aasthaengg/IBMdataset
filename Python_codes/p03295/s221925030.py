n, m = map(int, input().split())
Island = []
for i in range(m):
    Island.append(list(map(int, input().split())))
Island.sort(key=lambda x: x[0])

g_bridge_start = 0
g_bridge_end = 0
total = 0

for i in range(m):
    bridge_start = Island[i][0]
    bridge_end = Island[i][1] - 1
    #print(bridge_start, bridge_end, g_bridge_start, g_bridge_end)
    if bridge_start <= g_bridge_end:
        g_bridge_start = max(g_bridge_start, bridge_start)
        g_bridge_end = min(g_bridge_end, bridge_end)
    else:
        g_bridge_start = bridge_start
        g_bridge_end = bridge_end
        total += 1
print(total)