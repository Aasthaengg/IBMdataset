from itertools import accumulate
from operator import sub
N, C = map(int, input().split())
X, V = map(list, zip(*[tuple(map(int, input().split())) for _ in range(N)]))
VA = list(accumulate([0]+V))
VR = list(accumulate([0]+V[::-1]))
XR = [0]+list(map(lambda x:C-x, X[::-1]))
X = [0]+X
VA = list(accumulate(map(sub, VA, X), max))
VR = list(accumulate(map(sub, VR, XR), max))
print(max(VA[i]+VR[N-i]-min(X[i], XR[N-i]) for i in range(N+1)))