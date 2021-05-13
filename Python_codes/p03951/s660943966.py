n = int(input())
S1 = input()
S2 = input()
ans = 2 * n
for i in range(1,n + 1):
    if S1[n - i:] == S2[:i]:
        ans = min((n - i) * 2 + i,ans)
print(ans)