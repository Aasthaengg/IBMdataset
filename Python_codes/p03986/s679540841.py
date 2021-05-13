# https://atcoder.jp/contests/agc005/tasks/agc005_a

S = input()
ret = len(S)
stack = []
for s in S:
    if s == 'S':
        stack.append(S)
    if s == 'T' and stack:
        stack.pop()
        ret -= 2

print(ret)