N = int(input())
A = list(map(int, input().split()))
odd = 1
for i in range(N):
    if A[i] % 2 == 0:
        odd *= 2
print(3**N - odd)