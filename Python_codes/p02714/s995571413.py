N = int(input())
S = input()
R = set()
G = set()
B = set()
for i in range(N):
    if S[i] == 'R':
        R.add(i)
    elif S[i] == 'G':
        G.add(i)
    else:
        B.add(i)

ans = len(R)*len(G)*len(B)
if ans == 0:
    print(0)
    exit()
for i in R:
    for j in G:
        d = abs(j-i)
        a = min(i, j)-d
        b = (i+j)/2
        c = max(i, j)+d
        s = {a, b, c}
        for k in s:
            if k in B:
                ans -= 1
print(ans)
