X, Y = map(int, input().split())

A = (2*Y - X)/3
B = (2*X - Y)/3
if (2*Y - X) % 3 != 0 or (2*X - Y) % 3 != 0 or A < 0 or B < 0:
    ans = 0
    print(ans)
else:
    A = int(A)
    B = int(B)
    p = 10**9 + 7
    def comb(n, r, p):
        num1, num2 = 1, 1
        for i in range(r):
            num1 *= n-i
            num2 *= i+1
            num1 %= p
            num2 %= p
        return int(num1 * pow(num2, p-2, p))
    ans = comb(A+B, A, p)
    print(ans % p)
