N = int(input())
s1 = input()
s2 = input()
p = 0
n = 0
ans = 1
while n < N:
    if p == 1:
        if s1[n] == s2[n]:
            ans *= 2
            n += 1
        else:
            ans *= 2
            n += 2
            p = 2
    elif p == 2:
        if s1[n] == s2[n]:
            # ans *= 1
            n += 1
            p = 1
        else:
            ans *= 3
            n += 2
    else:
        if s1[n] == s2[n]:
            ans *= 3
            n += 1
            p = 1
        else:
            ans *= 6
            n += 2
            p = 2
    ans %= 1000000007
    # print(n, ans)
print(ans)
