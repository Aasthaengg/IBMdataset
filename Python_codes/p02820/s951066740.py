N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
def jan(a):
    if a == 'r':
        return P
    elif a == 's':
        return R
    else:
        return S
ans = 0
for i in range(K):
    check = 'n' + T[i::K]
    h = 0
    for i in range(len(check)-1):
        if check[i] != check[i+1]:
            ans += jan(check[i+1])
            h = 0
        else:
            if h == 0:
                h = 1
            else:
                ans += jan(check[i+1])
                h = 0
print(ans)