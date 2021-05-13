N = int(input())

# Nの因数を昇順で返す関数。1含む
def factor(n):
    f = []
    for i in range(1, int(n**0.5) + 1):
        if n%i == 0:
            f.append(i)
            if i != n//i:
                f.append(n//i)
    return f

ans = 0
for x in factor(N):
    m = (N//x) - 1
    if x < m:
        ans += m

print(ans)