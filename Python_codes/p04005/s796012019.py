s = [int(s) for s in input().split()]

if any([n % 2 == 0 for n in s]):
    print(0)
else:
    s[s.index(max(s))] = 1
    print(s[0] * s[1] * s[2])