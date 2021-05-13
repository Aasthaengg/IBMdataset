def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    ans = 0
    pre = 0
    for i in A:
        if pre < i:
            ans += i-pre
        pre = i
    
    return ans

print(solve())