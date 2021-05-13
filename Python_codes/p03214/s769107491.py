N = int(input())
A = list(map(int, input().split()))

# avg = sum(A) / N
sum_a = sum(A)
ans = float('inf')
ansf = -1
for i, ai in enumerate(A):
    # diff = abs(ai - avg)
    diff = abs(N * ai - sum_a)
    if diff < ans:
        ans = diff
        ansf = i

print(ansf)