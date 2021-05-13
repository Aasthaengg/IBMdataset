n = int(input())
s = [input() for _ in range(2)]

ans = 1
mod = 1000000007
count = 0
flag = True

while count < n:
    if count == 0:
        if s[0][count] == s[1][count]:
            ans *= 3
            count += 1
        else:
            ans *= 3 * 2
            count += 2
            flag = False
    else:
        if flag:
            if s[0][count] == s[1][count]:
                ans *= 2
                count += 1
            else:
                ans *= 2 * 1
                count += 2
                flag = False
        else:
            if s[0][count] == s[1][count]:
                ans *= 1
                count += 1
                flag = True
            else:
                ans *= 3
                count += 2
    ans %= mod

print(ans)
