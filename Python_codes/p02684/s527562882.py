N, K = map(int, input().split())
A = list(map(int, input().split()))

timestep_pos_map = []  # (i -> n)
pos_timestep_map = {}  # (n -> i)

timestep_pos_map.append(1)  # start
pos_timestep_map[1] = 0     # start

for timestep in range(1, min(K + 1, N + 1 + 1)):
    prev_pos = timestep_pos_map[-1]
    cur_pos = A[prev_pos - 1]

    if timestep == K:
        print(cur_pos)
        exit()

    if cur_pos in pos_timestep_map:
        prev_timestep = pos_timestep_map[cur_pos]
        interval = timestep - prev_timestep
        offset = (K - prev_timestep) % interval
        print(timestep_pos_map[prev_timestep + offset])
        exit()

    timestep_pos_map.append(cur_pos)
    pos_timestep_map[cur_pos] = timestep
