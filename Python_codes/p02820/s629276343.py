N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = input()

ans = 0
for k in range(K):
    t = T[k::K]
    b = 'a'
    for i in range(len(t)):
        if t[i] == b:
            b = 'a'
        else:
            if t[i] == 'r':
                ans += P
            elif t[i] == 's':
                ans += R
            else:
                ans += S
            b = t[i]
print(ans)