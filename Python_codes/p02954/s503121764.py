S = input()
S = S.replace("LR", "L,R")
S_list = S.split(",")
def counter(S):
    S_left_right = S.split("RL")
    S_left = S_left_right[0]
    S_right = S_left_right[1]
    num_R = len(S_left)
    num_L = len(S_right)
    num_center = [1, 1]
    num_center[0] += num_R // 2
    num_center[1] += num_R - num_R // 2
    num_center[0] += num_L - num_L // 2
    num_center[1] += num_L // 2
    return_list = [0] * num_R + num_center + [0] * num_L
    return return_list
ans = []
for string in S_list:
    ans += counter(string)
print(*ans)