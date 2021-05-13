from itertools import groupby
N=input()
S=list(groupby(N))
print(len(S)-1)