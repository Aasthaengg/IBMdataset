N = input()
ans = 'No'
for i in range(1, len(N) - 1):
    if N[i - 1] == N[i] and N[i] == N[i + 1]:
        ans = 'Yes'
print(ans)