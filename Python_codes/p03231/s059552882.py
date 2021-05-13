import functools, fractions
def lcm(a, b):
	return a * b // fractions.gcd(a, b)
def check(L, NM):
    res = []
    for i in range(NM):
        res.append(int(i*(L/NM)+1))
    return res
def check2(x, L, NM):
    return int((x-1)*NM/L)
def main():
    N,M = map(int,input().split())
    S = input()
    T = input()
    L = lcm(N,M)
    ans = L
    a = list(set(check(L, N)) & set(check(L, M)))
    for i in a:
        if S[check2(i, L, N)] != T[check2(i, L, M)]:
            ans = -1
            break
    print(ans)
if __name__ == '__main__':
    main()