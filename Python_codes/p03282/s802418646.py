S = input()
K = int(input())

ans = 1
for i in range(K):
    if int(S[i]) != 1:
        ans = S[i]
        break
print(ans)
