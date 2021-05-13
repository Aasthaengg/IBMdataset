S = input()
N = len(S)

ans = 0
for i in range(2 ** (N - 1)):
    nums = []
    num = ''
    for j in range(N):
        num += S[j]
        if (i >> j) & 1:
            nums.append(int(num))
            num = ''
    else:
        nums.append(int(num))
    ans += sum(nums)

print(ans)
