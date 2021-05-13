S = input()

ans = 10**4
for i in range(len(S) - 2):
    a = abs(int(S[i: i + 3]) - 753)
    if a < ans:
        ans = a
print(ans)
