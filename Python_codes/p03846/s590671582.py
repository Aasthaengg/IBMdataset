n = int(input())
alst = list(map(int, input().split()))
num = n - 1
ans_lst = [abs(i) for i in range(-num, num + 1, 2)]
alst.sort()
ans_lst.sort()
if alst != ans_lst:
    print(0)
else:
    MOD = 10 ** 9 + 7
    ans = pow(2, n // 2, MOD)
    print(ans)