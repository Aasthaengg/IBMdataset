N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7

if N % 2 == 1:

    memo = {key:0 for key in [i for i in range(2, N, 2)]}

    for a in A:
        try:
            memo[a] += 1
        except:
            memo[a] = 1

# print(memo)

    check_list = {}
    for i in range(2, N, 2):
        check_list[i] = False

    for check_num in check_list.keys():
        if check_num == 0:
            if memo[check_num] != 1:
                print(0)
                quit()
        if memo[check_num] != 2:
            print(0)
            quit()

else:
    memo = {key:0 for key in [i for i in range(1, N, 2)]}

    for a in A:
        try:
            memo[a] += 1
        except:
            memo[a] = 1

# print(memo)

    check_list = {}
    for i in range(1, N, 2):
        check_list[i] = False

    for check_num in check_list.keys():
        if memo[check_num] != 2:
            print(0)
            quit()

ans = pow(2, len(check_list))
ans %= mod
print(ans)
