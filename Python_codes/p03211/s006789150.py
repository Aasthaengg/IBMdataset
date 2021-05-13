S=input()
n=len(S)
ans = 1e8
for i in range(n-2):
    m = int(S[i] + S[i+1] + S[i+2])
    d = abs(m-753)
    if d < ans:
        ans = d
print(ans)