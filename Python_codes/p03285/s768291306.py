N = int(input())
ans = "No"
for i in range(N // 7 + 1):
    for j in range((N - i*7) // 4 + 1):
        if 7*i + 4*j == N:
            ans = "Yes"
print(ans)