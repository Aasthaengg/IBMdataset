a, b, c, d = map(int, input().split())

one = a * b
two = c * d

print(*max([one],[two]))