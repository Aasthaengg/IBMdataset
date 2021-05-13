s = input()
t = input()

l = len(t)
n = len(s) - len(t)

def count_diffs(lhs, rhs):
    return len(list(filter(lambda t: t[0] != t[1], zip(lhs, rhs))))

min_diff = l

for i in range(n):
    diff = count_diffs(s[i : i + l], t)

    if diff < min_diff:
        min_diff = diff

if n != 0:
    print(min_diff)

else:
    print(count_diffs(s, t))
