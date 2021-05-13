S = input()
N = len(S)
ans = num_a = 0

pre_is_a = True
i = 0
while i < N:
    s = S[i]
    if s == 'A':
        pre_is_a = True
        num_a += 1
    elif s == 'B' and pre_is_a:
        num_bc = 0
        flag = True
        for j in range(i, N-1, 2):
            if S[j:j+2] == 'BC':
                num_bc += 1
            else:
                flag = False
                break
        if num_bc:
            ans += num_a * num_bc
            if flag:
                i = N
            else:
                i = j - 1
        else:
            pre_a = False
            num_a = 0
    else:
        pre_a = False
        num_a = 0

    i += 1

print(ans)