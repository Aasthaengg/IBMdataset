S = input()
N = len(S) - 1

ans = 0
for i in range(2 ** N):
    add_pos = []
    for j in range(N):
        if (i >> j) & 1:
            add_pos.append(j + 1)

    to_be_sumed = []

    if not add_pos:
        to_be_sumed.append(int(S))

    for i in range(len(add_pos)):
        if i == 0:
            to_be_sumed.append(int(S[:add_pos[i]]))
            if i == len(add_pos) - 1:
                to_be_sumed.append(int(S[add_pos[i]:]))
        else:
            to_be_sumed.append(int(S[add_pos[i - 1]:add_pos[i]]))
            if i == len(add_pos) - 1:
                to_be_sumed.append(int(S[add_pos[i]:]))
    # print(to_be_sumed)
    ans += sum(to_be_sumed)
print(ans)
