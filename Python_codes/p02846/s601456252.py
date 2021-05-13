T = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
if T[0]* A[0] + T[1] * A[1] == T[0] * B[0] + T[1] * B[1]:
    print('infinity')
else:
    ans = 0
    A_pos = 0
    B_pos = 0
    before_state = -1 # 0:A>B, 1:A < B, -1:A=B
    flag = True
    diff = abs(T[0]* A[0] + T[1]* A[1] - (T[0]* B[0] + T[1]* B[1]))
    diff_max = max(abs(A[0] - B[0])*T[0],  abs(A[1] - B[1])*T[1])
    max_num = int(diff_max/diff)
    up_num_first = 0
    for i in range(2):
        A_pos += T[i]* A[i]
        B_pos += T[i]* B[i]
        if A_pos > B_pos:
            if before_state == 0:
                up_num_first += 1
            before_state = 1
        elif A_pos < B_pos:
            if before_state == 1:
                up_num_first += 1
            before_state = 0
        elif A_pos == B_pos:
            up_num_first += 1
            before_state = -1
    A_pos_first = A_pos
    B_pos_first = B_pos
            
    up_num_second = 0
    for i in range(2):
        A_pos += T[i]* A[i]
        B_pos += T[i]* B[i]
        if A_pos > B_pos:
            if before_state == 0:
                up_num_second += 1
            before_state = 1
        elif A_pos < B_pos:
            if before_state == 1:
                up_num_second += 1
            before_state = 0
        elif A_pos == B_pos:
            up_num_second += 1
            before_state = -1

    A_pos = A_pos_first * (max_num - 1)
    B_pos = B_pos_first * (max_num - 1)
    up_num_final = 0
    for i in range(2):
        A_pos += T[i]* A[i]
        B_pos += T[i]* B[i]
        if A_pos > B_pos:
            if before_state == 0:
                up_num_final += 1
            before_state = 1
        elif A_pos < B_pos:
            if before_state == 1:
                up_num_final += 1
            before_state = 0
        elif A_pos == B_pos:
            up_num_final += 1
            before_state = -1
    if max_num > 1:
        ans = up_num_first  + (max_num - 2) * up_num_second  + up_num_final
    else:
        ans = up_num_first  + (max_num - 1) * up_num_second
    print(ans)