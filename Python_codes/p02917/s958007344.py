N = int(input())
B = list(map(int, input().split()))
S = B[0] + B[N-2]
i = 0
while i <= N-3:
    if B[i] > B[i+1]:
        S += B[i+1]
    else:
        S += B[i]
    i += 1
print(S)