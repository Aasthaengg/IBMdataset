hours_p_distance, hours_q_distance, hours_r_distance = map(int, input().split())

root_p_q = hours_p_distance + hours_q_distance
root_p_r = hours_p_distance + hours_r_distance
root_q_r = hours_q_distance + hours_r_distance

if hours_p_distance == 0 or hours_q_distance == 0 or hours_r_distance == 0:
    print(max(root_p_q, root_p_r, root_q_r))
else:
    print(min(root_p_q, root_p_r, root_q_r))