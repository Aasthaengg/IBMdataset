# 数のbitに含まれる1の数をカウント
def bitsoncount(x):
    return bin(x).count('1')

def solve(x):
    global ans
    bx = bitsoncount(x)
    if bx == 0:
        return ans
    else:
        ans += 1
        x = x % bx
        solve(x)


N = int(input())
X = input()

Xb = bitsoncount(int(X, 2))
if (Xb - 1) != 0:
    X0 = int(X, 2) % (Xb-1)
X1 = int(X, 2) % (Xb+1)

for x, i in zip(X, reversed(range(N))):
    x = int(x)
    if x == 0:
        temp = (X1 + pow(2, i, Xb+1)) % (Xb+1)
        ans = 1
    else:
        if Xb - 1 == 0:
            print(0)
            continue
        temp = (X0 - pow(2, i, Xb-1)) % (Xb-1)
        ans = 1
    
    solve(temp)
    print(ans)