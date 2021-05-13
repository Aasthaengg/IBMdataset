n = int(input())
A = [int(input()) for _ in range(n)]
f_num = max(A)
A_c = A.copy()
A_c.remove(f_num)
s_num = max(A_c)

for a in A:
    if a == f_num:
        print(s_num)
    else:
        print(f_num)