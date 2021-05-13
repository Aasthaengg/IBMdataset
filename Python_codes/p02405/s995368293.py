# ?????§?????????????????????
import sys

pattern = ['#', '.']

while True:
    data = sys.stdin.readline().strip().split(' ')
    h = int(data[0])
    w = int(data[1])

    if h == 0 and w == 0:
        break

    pat_idx = 0
    st_pat_idx = 0
    for i in range(h):
        for j in range(w):
            print(pattern[pat_idx], end='')
            pat_idx = 1 - pat_idx # pat_idx <- 0, 1, 0, 1...?????°?????????

        st_pat_idx = 1 - st_pat_idx
        pat_idx = st_pat_idx
        print('')

    print('')