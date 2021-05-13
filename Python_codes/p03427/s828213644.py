# https://atcoder.jp/contests/agc021/tasks/agc021_a

n = input()
if int(n) >= int(n[0] + '9' * (len(n) - 1)):
    ans = int(n[0]) + 9 * (len(n) - 1)
else:
    ans = int(n[0]) - 1 + 9 * (len(n) - 1)
print(ans)