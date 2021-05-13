N = int(input())
A,B = list(map(int,input().split()))
P = list(map(int,input().split()))
AA = 0
AB = 0
BB = 0
for i in range(N):
    if P[i] <= A:
        AA += 1
    elif A+1 <= P[i] <= B:
        AB += 1
    else:
        BB += 1
print(min(AA,AB,BB))