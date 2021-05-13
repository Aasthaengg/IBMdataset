import collections

N = int(input())
A = [int(i) for i in input().split()]
ans = 0
di = collections.Counter(A)
if N % 2 != 0:
    num_list = [int(i) for i in range(2, N, 2)]
    for num in num_list:
        if di[num] != 2:
            break
    else:
        if A.count(0) == 1:
            ans = (2 ** (N // 2)) % (10 ** 9 + 7)

else:
    num_list = [int(i) for i in range(1, N, 2)]
    for i in num_list:
        if di[i] != 2:
            break
    else:
        ans = (2 ** (N // 2)) % (10 ** 9 + 7)
print(ans)