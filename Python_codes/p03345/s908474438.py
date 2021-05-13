import math
A, B, C, K = map(int, input().split())

abs_ans = abs(A-B)

if A <= B:
    if K % 2 == 0:
        print(-abs_ans)
    else:
        print(abs_ans)
else:
    if K % 2 == 0:
        print(abs_ans)
    else:
        print(-abs_ans)