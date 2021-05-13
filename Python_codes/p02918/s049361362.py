N, K = [int(_c) for _c in input().split(" ")]
S_orig = input()
point_list = []
for target, non_target in zip(["L", "R"], ["R", "L"]):
    S = list(S_orig)

    start_idx_list = []
    before_char = None
    for i, c in enumerate(S):
        if i == 0:
            start_idx_list.append(i)
            before_char = c
        else:
            if before_char == non_target and c == target:
                start_idx_list.append(i)
            before_char = c
    start_idx_list.append(len(start_idx_list) - 1)
    if len(start_idx_list) - 1 <= K:
        point_list.append(len(S) - 1)
        continue

    longest = 0
    start_idx = -1
    end_idx = -1
    for i in range(len(start_idx_list) - K):
        cur_length = start_idx_list[i + K] - start_idx_list[i] + 1
        if cur_length > longest:
            start_idx = start_idx_list[i]
            end_idx = start_idx_list[i + K]
            longest = cur_length

    for _idx in range(start_idx, end_idx):
        S[_idx] = target
    S = ["N"] + S + ["N"]

    point = 0
    for idx in range(1, N + 1):
        if S[idx] == "L":
            if S[idx + 1] == "L":
                point += 1
        if S[idx] == "R":
            if S[idx - 1] == "R":
                point += 1

    point_list.append(point)

print(max(point_list))