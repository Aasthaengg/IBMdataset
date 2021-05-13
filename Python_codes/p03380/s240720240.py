import sys
input = sys.stdin.readline

n = int(input())
a = [int(x) for x in input().split()]
N = max(a)

if N % 2 == 0:
    ans = N // 2
    dis = 10**18
    ans_ = N
    for i in a:
        if abs(i - ans) <= dis:
            dis = abs(i - ans)
            ans_ = i
    print(N, ans_)

else:
    ans1 = N // 2
    ans2 = ans1 + 1
    ans_ = N
    dis = 10**18
    for i in a:
        if abs(i -ans1) <= dis:
            dis = abs(i - ans1)
            ans_ = i
        if abs(i - ans2) <= dis:
            dis = abs(i - ans2)
            ans_ = i
    print(N, ans_)
