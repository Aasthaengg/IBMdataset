def f(s):
    return len({x for x in s}) == 1

N = input()
print('Yes' if f(N[:3]) or f(N[1:]) else 'No')
