A, B, C = map(int, input().split())
s = sorted([A, B, C])
a = s[2] - s[0]
b = s[2] - s[1]

a_odd = a % 2 == 1
b_odd = b % 2 == 1

ans = a // 2 + b // 2

if a_odd and b_odd:
    ans += 1
elif a_odd and not b_odd:
    ans += 2
elif not a_odd and b_odd:
    ans += 2

print(ans)