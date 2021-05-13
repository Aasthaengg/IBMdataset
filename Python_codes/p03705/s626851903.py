N, A, B = map(int, input().split())
if N == 0 or A > B:
    print(0)
    quit()
if N == 1 and A != B:
    print(0)
    quit()
minSum = A * (N-1) + B
maxSum = A + B * (N-1)
print(maxSum-minSum+1)