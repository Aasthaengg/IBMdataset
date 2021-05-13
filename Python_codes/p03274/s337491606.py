N, K = map(int, input().split())
X = list(map(int, input().split()))
check_X = X[0:K]

def calc_distance(check_X):
    if check_X[0] * check_X[-1] < 0:
        result = min(abs(check_X[0]*2)+abs(check_X[-1]), abs(check_X[0])+abs(check_X[-1]*2))
    else:
        result = max(abs(check_X[0]),abs(check_X[-1]))
    return result

ans = calc_distance(check_X)

for i in range(K, len(X)):
    check_X.pop(0)
    check_X.append(X[i])
    ans = min(ans, calc_distance(check_X))

print(ans)
