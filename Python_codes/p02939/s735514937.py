s = input()

res = [s[0]]
it = iter(s[1:])
for c in it:
    if res[-1] == c:
        try:
            res.append(c + next(it))
        except StopIteration:
            res[-1] += c
    else:
        res.append(c)

print(len(res))
