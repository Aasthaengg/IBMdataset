N  = int (input())
nums = list(map(int, input().split(" ")))
colors = [0,0,0]
ans = 1
MOD = 10 ** 9 + 7
for num in nums:
    cot = 0
    ind = -1
    for i in range(3):
        if colors[i] == num:
            ind = i
            cot += 1
    colors[ind] += 1
    ans *= cot
    ans %= MOD
print(ans)