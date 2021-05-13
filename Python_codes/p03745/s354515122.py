N = int(input())
A = list(map(int, input().split()))

now = False
count = 1
for i in range(N-1):
    if A[i] < A[i+1]:
        if now == 1:
            pass
        elif now == -1:
            count += 1
            now = False
        else:
            now = 1
    elif A[i] > A[i+1]:
        if now == 1:
            count += 1
            now = False
        elif now == -1:
            pass
        else:
            now = -1

print(count)