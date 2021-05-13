import collections

S=list(input())
ABC=[chr(i) for i in range(97,123)]
N=len(S)
_S=collections.Counter(S)
a=int(N*(N-1)/2-sum([_S[s]*(_S[s]-1)/2 for s in _S]) + 1)
print(a)
