N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ABdiff = sorted([A[i]-B[i] for i in range(N)], reverse = True)
if sum(ABdiff) < 0:
    print(-1)
    exit()

ABminus = [A[i]-B[i] for i in range(N) if A[i]-B[i] < 0]
if len(ABminus) == 0:
    print(0)
    exit()

all_minus = sum(ABminus)
plus = 0

for i in range(N):
    plus += ABdiff[i]
    if plus >= abs(all_minus):
        print(i+1 + len(ABminus))
        break