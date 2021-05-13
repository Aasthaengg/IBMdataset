S = list(input())
ans = 0

for i in range(2**(len(S)-1)):
    tmp = S
    p = list(bin(i))
    flag = ['0' for _ in range(len(S) - len(p) + 1)] + p[2:]
    nums = []
    l = 0
    for j in range(len(S)-1):
        if flag[j] == '1':
            nums.append("".join(tmp[l:j+1]))
            l = j+1
    nums.append("".join(tmp[l:]))
    for n in nums:
        ans += int(n)

print(ans)
