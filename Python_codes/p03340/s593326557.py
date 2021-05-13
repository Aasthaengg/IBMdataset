import sys
input = sys.stdin.readline

N = int(input())
A = [int(i) for i in input().split()]

answer = 0
right = 0
lrsum = 0
for left in range(N):
    while right < N and (lrsum ^ A[right]) == (lrsum + A[right]):
        lrsum += A[right]
        right += 1
    answer += right - left
    if left == right:
        right += 1
    else:
        lrsum -= A[left]

print(answer)