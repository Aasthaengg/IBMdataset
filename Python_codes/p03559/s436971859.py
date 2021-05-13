from bisect import bisect_left
from bisect import bisect_right

N = int(input())
A = list(map(int, input().split()))
A.sort()
B = list(map(int, input().split()))
C = list(map(int, input().split()))
C.sort()


X = [bisect_left(A ,B[i]) for i in range(N)]
Y = [N - bisect_right(C ,B[i]) for i in range(N)]

total = 0

for x,y in zip(X, Y):
    total += x * y

print(total)