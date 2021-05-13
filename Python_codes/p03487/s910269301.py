import numpy as np

# input
N = int(input().split()[0])
sequence = np.array(list( map(int, input().split()) ))

# a_N>N must be removed
remove = np.sum(sequence>N)
sequence = sequence[sequence<=N]

index = np.unique(sequence)

for idx in index:

    n_idx = np.sum(sequence==idx)
    if n_idx < idx:
        remove += n_idx
    else:
        remove += (n_idx-idx)

print(remove)


