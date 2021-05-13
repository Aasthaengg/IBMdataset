# https://atcoder.jp/contests/agc005/tasks/agc005_a

x = input()
ans = len(x)
stack = []
for i in range(len(x)):
    if x[i] == 'S':
        stack.append(x[i])
    elif x[i] == 'T' and stack:
        ans -= 2
        stack.pop()
print(ans)