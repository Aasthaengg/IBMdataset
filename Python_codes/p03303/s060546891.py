def solve(s, w):
    return "".join([s[i] for i in range(0, len(s), w)])

s = input()
w = int(input())
print(solve(s, w))
