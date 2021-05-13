S = input()
K = int(input())

ans = ''
for s in S:
    to_a_cost = (26 - (ord(s) - 97)) % 26
    if to_a_cost <= K:
        ans += 'a'
        K -= to_a_cost
    else:
        ans += s


if K:
    K %= 26
    ans = ans[:-1] + chr(97 + (((ord(ans[-1]) - 97) + K) % 26))

print(ans)
