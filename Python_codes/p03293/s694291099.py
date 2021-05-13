def actual(s, t):
    """
    kyoto
    okyot
    tokyo
    otoky
    yotok
    kyoto
    """
    for _ in range(len(s)):
        s = s[-1] + s[:-1]

        if s == t:
            return 'Yes'

    return 'No'

s = input()
t = input()

print(actual(s, t))