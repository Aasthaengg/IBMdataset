A = [int(input()) for _ in range(5)]
k = int(input())
ans = 'Yay!'
for i in range(len(A)):
    for j in range(len(A)):
        if i == j:
            continue
        if abs(A[i] - A[j]) > k:
            ans = ':('
print(ans)