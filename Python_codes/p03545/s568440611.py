S = input()
A, B, C, D = [int(s) for s in S]
op_l = ["+", "-"]

ex = ""
for op_1 in op_l:
    for op_2 in op_l:
        for op_3 in op_l:
            ans = A + B if op_1 == "+" else A - B
            ans = ans + C if op_2 == "+" else ans - C
            ans = ans + D if op_3 == "+" else ans - D
            if ans == 7:
                ex = str(A) + op_1 + str(B) + op_2 + str(C) + op_3 \
                     + str(D) + "=7"

print(ex)