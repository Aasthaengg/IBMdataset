import bisect

N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]

A.sort()
B.sort()
C.sort()

numpattern = 0

for i in range(N):
    numsmallerA = bisect.bisect_left(A,B[i])
    numbiggerC = N - bisect.bisect_right(C,B[i])
    numpattern += numsmallerA * numbiggerC

print(numpattern)