# https://atcoder.jp/contests/agc005/tasks/agc005_a
#
# Stackでやる

from collections import deque

stack = deque([])
X = input()

for ch in X:
    if ch == 'S':
        stack.append(ch)
    elif ch == 'T':
        if len(stack) == 0:
            stack.append(ch)
        elif stack[-1] == 'T':
            stack.append(ch)
        elif stack[-1] == 'S':
            stack.pop()

print(len(stack))