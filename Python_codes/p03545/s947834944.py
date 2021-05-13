import sys
N = input()
A = int(N[0])
B = int(N[1])
C = int(N[2])
D = int(N[3])

def ops (i):
    ans = "+" if i == 0 else "-"
    return ans

for i in range(2):
    for j in range(2):
        for k in range(2):
            ans = A + ((-1)**i)*B + ((-1)**j)*C + ((-1)**k)*D

            if ans == 7:
                print("{0}{1}{2}{3}{4}{5}{6}=7" .format(A,ops(i),B,ops(j),C,ops(k),D))
                sys.exit()