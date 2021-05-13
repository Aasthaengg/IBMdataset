import collections

N, K = map(int, input().split())
A = sorted(collections.Counter(list(map(int, input().split()))).items(), key=lambda x: x[1], reverse = True)
if len(A) <= K:
    print(0)
else:
    print(sum([x[1] for x in A[K:]]))