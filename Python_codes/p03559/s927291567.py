import bisect
N = int(input())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))
C = sorted(list(map(int, input().split())))
result = 0
for b in B:
    #print(search(A, b-1, True) + 1, N - search(C, b+1, False))
    result += bisect.bisect_right(A, b - 1) * (N-bisect.bisect_left(C, b + 1))
print(result)