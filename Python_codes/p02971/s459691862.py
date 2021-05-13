import sys
N = int(input())
A = [int(sys.stdin.readline()) for _ in range(N)]
sortedA = sorted(A, reverse=True)
for a in A:
    if a == sortedA[0]:
        print(sortedA[1])
    else:
        print(sortedA[0])