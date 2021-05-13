def solve():
    N = int(input())
    for h in range(1,3500+1):
        for n in range(1,3500+1):
            numerator = N * h * n
            denominator = 4 * h * n - N * n - N * h

            if denominator == 0:
                continue

            w = numerator // denominator
            if numerator % denominator == 0 \
            and 0 < w <= 3500:
                print(h,n,w)
                return
        
if __name__ == '__main__':
    solve()
