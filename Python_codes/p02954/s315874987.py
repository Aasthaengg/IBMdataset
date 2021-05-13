
S = input()

ans = [0] * len(S)

P = "R"
B = 0
L_cnt = 1
R_cnt = 0
cnt = 0

for i in range(1, len(S)):
    if P == "R":
        if S[i] == "R":
            R_cnt += 1
            temp = R_cnt
            R_cnt = L_cnt
            L_cnt = temp

        else:
            B = i
            ans[B - 1] += L_cnt
            ans[B] += R_cnt

            # reset
            L_cnt = 1
            R_cnt = 0
            ans[B] += 1
            P = "L"

    elif P == "L":
        cnt += 1

        if S[i] == "L":
            if cnt % 2 == 1:
                ans[B-1] += 1
            else:
                ans[B] += 1

        else:
            # reset
            cnt = 0
            P = "R"

print(*ans)
