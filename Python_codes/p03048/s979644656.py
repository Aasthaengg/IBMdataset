# from pprint import pprint
# import math
# import collections

# n = int(input())
R, G, B, N = map(int, input().split(' '))
# a = list(map(int, input().split(' ')))

# max_r, max_g, max_b = N // R, N // G, N // B
ans = []

r, g, b = 0, 0, 0
cnt = 0

max_r = N // R
for r in range(max_r + 1):
    if R * r > N:
        break

    max_g = (N - R * r) // G

    for g in range(max_g + 1):
        if R * r + G * g > N:
            break
        x = (N - (R * r + G * g))
        if x % B == 0 and x >= 0:
            # b = x // B
            # a = (r, g, b)
            cnt += 1
            # ans.append(a)

# print(len(ans))
print(cnt)
