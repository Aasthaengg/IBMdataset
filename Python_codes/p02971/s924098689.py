N = int(input())
A = []
for i in range(N):
    A.append(int(input()))
import copy
B = copy.deepcopy(A)
A = sorted(A)
for i in range(N):
    num = B[i]
    if num != A[-1]:
        print(A[-1])
    else:
        print(A[-2])