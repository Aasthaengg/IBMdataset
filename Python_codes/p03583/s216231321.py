# 4/N = 1/h + 1/n + 1/w
# 4*h*n*w = N*(nw+hn+wh) = N*(h+n)*w + N*hn
# (4*h*n - N*(h+n))*w = N*hn

# 4*h*n > N*(h+n)

L=3501
N=int(input())
def solve():
    for h in range(1,L):
        for n in range(1,h):
            d = 4*h*n - N*(h+n)
            if d > 0 and N*h*n % d == 0:
                print(h,n,N*h*n // d)
                return
solve()
