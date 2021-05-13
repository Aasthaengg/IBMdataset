S = input()

l = len(S) - 2
min_diff = float("inf")
for i in range(0, l):
    num = int(S[i:i+3])
    diff = abs(753 - num)
    if min_diff > diff:
        min_diff = diff

print(min_diff)