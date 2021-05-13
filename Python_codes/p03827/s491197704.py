N = int(input())
S = input()

x = 0
max_x = 0
for c in S:
    x += 1 if c == "I" else -1
    max_x = max(x, max_x)

print(max_x)