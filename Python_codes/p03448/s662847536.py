# import numpy as np

A_init = 500
B_init = 100
C_init = 50

A_n = int(input())
B_n = int(input())
C_n = int(input())

X = int(input())

cnt = 0
for a in range(A_n+1):
    if A_init * a <= X:
        for b in range(B_n+1):
            if (A_init * a + B_init * b) <= X:
                K = X - (A_init * a + B_init * b)
                if K % 50 == 0 and K / C_init <= C_n:
                    cnt += 1
            else:
                break
    else:
        break
# print(np.count_nonzero([k+[i for i in All_list] == X for k in All_list]))
print(cnt)