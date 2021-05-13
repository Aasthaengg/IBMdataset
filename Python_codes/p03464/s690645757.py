K = int(input())
A = list(map(int, input().split()))

ans1 = 2
ans2 = 2
for i in range(K - 1, 0, -1):
    if ans1 % A[i] != 0 or ans2 % A[i] != 0 or ans1 < 2 or ans2 < 2:
        print (-1)
        exit()
    ans1 = (ans1 + A[i] - 1) // A[i - 1] * A[i - 1] #最大
    ans2 = (ans2 + A[i - 1] - 1) // A[i - 1] * A[i - 1] #最小
    if ans2 > ans1: #逆転している = 存在できない
        print (-1)
        exit()

    # print (ans1, ans2)

if ans1 % A[0] != 0 or ans2 % A[0] != 0 or ans1 < 2 or ans2 < 2:
    print (-1)
    exit()

print (ans2, ans1 + A[0] - 1)    