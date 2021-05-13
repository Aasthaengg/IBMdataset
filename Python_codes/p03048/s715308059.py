R, G, B, N = map(int, input().split())
def solve():
    ans = 0
    for i in range(N//R+1):
        b1 = N - i*R
        for j in range(b1//G+1):
            b2 = b1 - j*G
            if b2%B==0:
                ans += 1
    return ans
print(solve())