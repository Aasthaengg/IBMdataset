import copy

s = input()
n = len(s)-1
ans = 0

for i in range(2 ** n):
    x = copy.deepcopy(s)
    y = 1
    for j in range(n):
        if ((i >> j) & 1): #フラグが立っていたら
            x = x[:j+y] + "+" + x[j+y:]
            y += 1
    ans += eval(x)

print(ans)