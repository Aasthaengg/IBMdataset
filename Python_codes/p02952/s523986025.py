def solve():
    ans = 0
    N = int(input())
    n = len(list(str(N)))
    if n%2==0:
        for i in range(1,n,2):
            ans += 10**(i-1)*9
    else:
        ans = N
        for i in range(2,n,2):
            ans -= 10**(i-1)*9
    return ans
print(solve())
