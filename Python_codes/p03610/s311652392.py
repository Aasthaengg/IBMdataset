# B - OddString
# https://atcoder.jp/contests/abc072/tasks/abc072_b

s = input()

result = ''
i = 0
while i < len(s):
    result += s[i]
    i += 2

print(result)
