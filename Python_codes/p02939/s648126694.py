s = input() + '*'

ans = 0
before_s = s[0]
i = 1

while i < len(s):
    if s[i] == before_s:
        # print('hi',before_s, s[i:i+2])
        before_s = s[i:i+2]
        ans += 1
        i += 2
    else:
        # print(i, before_s, s[i])
        before_s = s[i]
        ans += 1
        i += 1

print(ans)