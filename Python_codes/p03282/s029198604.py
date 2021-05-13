S = input()
K = int(input())

ans = '1'
for i in range(K):
    if S[i] != ans:
        ans = S[i]
        break

print(ans)