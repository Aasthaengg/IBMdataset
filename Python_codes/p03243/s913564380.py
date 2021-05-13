import sys
N = int(input())
if not (100 <= N <= 999):
    sys.exit()

answer = [111,222,333,444,555,666,777,888,999]
for I in range(N,1000):
    for J in answer:
        if I == J:
            print(I)
            sys.exit()
