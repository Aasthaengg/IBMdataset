MOD = 10**9 + 7
N = int(input())
a = input()
b = input()
ans = 0
i = 0
beforeState = True
while i < N:
    if i == 0:
        if a[i] == b[i]:
            ans = 3
            beforeState = True
        else:
            ans = 6
            i += 1
            beforeState = False
    else:
        if a[i] == b[i]:
            if beforeState:
                ans *= 2
            else:
                ans *= 1
            beforeState = True
        else:
            if beforeState:
                ans *= 2
            else:
                ans *= 3
            beforeState = False
            i += 1
    ans = ans%MOD
    i += 1
print(ans)