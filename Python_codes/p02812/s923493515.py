N = int(input())
S = list(input())

ans = 0
ref = ""
for i in range(N-2):
    ref = S[i] + S[i+1] + S[i+2]
    if ref == "ABC":
        ans += 1

print(ans)