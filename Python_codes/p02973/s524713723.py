import bisect
def get_LIS(seq):
    LIS = [seq[0]]
    for i in range(1,len(seq)):
        if seq[i] >= LIS[-1]:
            LIS.append(seq[i])
        else:
            LIS[bisect.bisect_right(LIS, seq[i])] = seq[i]

    print(len(LIS))


N = int(input())
A = [int(input()) for _ in range(N)]
A = A[::-1]
get_LIS(A)