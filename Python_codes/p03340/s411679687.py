import sys, os

f = lambda:list(map(int,input().split()))
if 'local' in os.environ :
    sys.stdin = open('./input.txt', 'r')


def c(r, l):
    cnt = r - l +1

    if cnt<2:
        return 0
    return cnt * (cnt-1)//2

def solve():
    n = f()[0]
    a = f()

    add_sum = 0
    xor_sum = 0
    ans = n

    l = 0
    r = 0
    while r<=n-1:
        add_sum += a[r]
        xor_sum ^= a[r]

        r+= 1

        if r == n and add_sum == xor_sum:
            ans += c(n-1, l)
            break

        if add_sum != xor_sum:
            nl = l
            while add_sum != xor_sum:
                add_sum -= a[nl]
                xor_sum ^= a[nl]
                nl += 1
            
            ans += c( nl-1, l)

            ans += (nl - l)*(r - nl-1)

            l = nl

        if r == n:
            ans += c(n-1, l)




    print(ans)

solve()
