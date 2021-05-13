ans = ""
N = int(input())
S = str(input())
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
M = len(abc)
for s in S:
    for i in range(M):
        if abc[i] == s:
            ans += abc[(i + N) % M]
print(ans)