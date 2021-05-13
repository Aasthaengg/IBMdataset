mod = 1000000007

n = int(input())
s1 = input()
s2 = input()

if s1[0] == s2[0]:
    ans = 3
    now = 1
    flag = True
else:
    ans = 6
    now = 2
    flag = False

while now < n:
    if flag:
        if s1[now] == s2[now]:
            ans *= 2
            ans %= mod
            now += 1
            flag = True
        else:
            ans *= 2
            ans %= mod
            now += 2
            flag = False
    else:
        if s1[now] == s2[now]:
            now += 1
            flag = True
        else:
            ans *= 3
            ans %= mod
            now += 2
            flag = False

print(ans)