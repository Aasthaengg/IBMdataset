A = [int(input()) for _ in range(5)]
K = int(input())

ans = "Yay!"
for i in range(5):
    for j in range(5):
        if A[i] - A[j] > K:
            ans = ":("

print(ans)
