n = int(input())
A = [None] + [int(i) for i in input().split()]

B = [0] * (n + 1)  # 1-indexed
ans = []

for i in range(1, n + 1)[::-1]:
    _tmp = sum(B[i * 2::i])
    if _tmp % 2 != A[i]:
        B[i] += 1
        ans.append(str(i))

print(len(ans))
print(" ".join(ans))
