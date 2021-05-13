N = int(input())
A = list(map(int, input().split()))

avg = sum(A) / N
ans = float('inf')
ansf = -1
for i, ai in enumerate(A):
    diff = abs(ai - avg)
    if diff < ans:
        ans = diff
        ansf = i

print(ansf)