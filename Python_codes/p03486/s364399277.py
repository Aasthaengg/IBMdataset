def actual(s, t):
    s = ''.join(sorted(s))
    t = ''.join(sorted(t, reverse=True))

    if s < t:
        return 'Yes'

    return 'No'

s = input()
t = input()

print(actual(s, t))