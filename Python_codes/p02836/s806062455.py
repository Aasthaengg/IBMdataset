import sys
input = sys.stdin.readline

s = input()[:-1]
print(sum([1 if s[i] != s[len(s) - i - 1] else 0 for i in range(len(s))]) // 2)