N = int(input())
A = [int(a) for a in input().split()] + [0]
B = [int(a) for a in input().split()] + [0]

MA = [0] * N
MI = [1] * N
P = 10**9+7
for i in range(N):
    if A[i] > A[i-1]:
        MA[i] = MI[i] = A[i]
    else:
        MA[i] = A[i]

for i in range(N)[::-1]:
    if B[i] > B[i+1]:
        if MI[i] <= B[i] <= MA[i]:
            MA[i] = MI[i] = B[i]
        else:
            print(0)
            exit()
    else:
        if B[i] >= MI[i]:
            MA[i] = min(MA[i], B[i])
        else:
            print(0)
            exit()
ans = 1
for i in range(N):
    ans = ans * (MA[i] - MI[i] + 1) % P
print(ans)