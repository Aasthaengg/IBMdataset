A, B = map(int, input().split())
a_cnt = 1
a_tmp = A
b_cnt = 1
b_tmp = B

while True:
    if a_tmp == b_tmp:
        print(a_tmp)
        exit(0)
    elif a_tmp > b_tmp:
        b_tmp = B*b_cnt
        b_cnt += 1
    else:
        a_tmp = A*a_cnt
        a_cnt += 1
