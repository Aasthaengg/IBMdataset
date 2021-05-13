import sys, os

f = lambda:list(map(int,input().split()))
if 'local' in os.environ :
    sys.stdin = open('./input.txt', 'r')



def solve():
    n = f()[0]
    a = f()

    add_sum = 0
    xor_sum = 0
    ans = 0

    l = 0
    r = 0
    while r<=n-1:
        add_sum += a[r]
        xor_sum ^= a[r]

        r+= 1

        if add_sum != xor_sum:
            while add_sum != xor_sum:
                add_sum -= a[l]
                xor_sum ^= a[l]
                ans += r - l-1
                l += 1

        if r == n:
            ans += (n-l+1)*(n-l)//2
    
    print(ans)


solve()
