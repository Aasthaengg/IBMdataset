S = input()
K = int(input())

not_1_idx = -1
not_1_num = 1
for i, c in enumerate(S):
    if c != "1":
        not_1_idx = i
        not_1_num = c
        break
if not_1_idx >= 0:
    print(1) if K < not_1_idx + 1 else print(not_1_num)
else:
    print(not_1_num)
