import collections
N = int(input())
A = [int(x) for x in input().split()]
A.sort(reverse=True)
B = []
i = 0
while i < N-1:
    if A[i]==A[i+1]:
        B.append(A[i])
        i += 2
    else:
        i += 1
if len(B)<2:
    print(0)
else:
    print(B[0] * B[1])