N = list(input())
ans = 0
for n in range(len(N)):
    if N[n] == "2":
        ans += 1
print(ans)