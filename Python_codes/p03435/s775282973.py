import numpy as np
IN = [list(map(int, input().split())) for _ in range(3)]
c = np.array(IN)
column = np.sum(c, axis=0)
row = np.sum(c, axis=1)
S = np.sum(c)
if S%3==0:
    S_ = S//3
    for i in range(S_+1):
        x = i
        y = S_ - x
        row_ = row - y
        column_ = column - x
        if all(col % 3 == 0 for col in column_) and all(ro % 3 == 0 for ro in row_):
            print("Yes")
            break
    else:
        print("No")
else:
    print("No")