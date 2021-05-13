s = [int(c) for c in input().split(' ')]

if s[0] > s[1] // 2:
    print(s[1] // 2)
else:
    print(s[0] + (s[1] - 2 * s[0]) // 4)