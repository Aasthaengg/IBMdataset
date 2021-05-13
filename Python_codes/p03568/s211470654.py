N = int(input())
A = list(map(int ,input().split()))

even = 0
odd = 0
for i in range(N):
    if A[i] % 2 == 0:
        even += 1
    else:
        odd += 1

if odd == N:
    ans = 3**N - 1
else:
    ans = 3**N - 2**even

print(ans)