N = int(input())
s, t = input(), input()

v = 0
for i in range(len(s)):
    # print(s[-(i + 1):], t[:i + 1])
    if s[-(i + 1):] == t[:i + 1]:
        v = i + 1
# print('v', v)
ans = N * 2 - v
print(ans)
