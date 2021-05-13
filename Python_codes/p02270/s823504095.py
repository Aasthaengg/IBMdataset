def check(p):
    i = 0
    for _ in range(k):
        s = 0
        while s+n_list[i] <= p:
            s += n_list[i]
            i += 1
            if i == n:
                return n
    return i

def solve():
    left   = 0
    right  = 10**5 * 10**4
    middle = 0
    while(right-left > 1):
        middle = (left+right)//2
        v = check(middle)
        if(v >= len(n_list)):
            right = middle
        else:
            left = middle
    return right

n,k = map(int,input().split())
n_list = [int(input()) for _ in range(n)]
ans = solve()
print(ans)
