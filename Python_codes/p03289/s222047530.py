def actual(s):
    # S の先頭の文字は大文字の A である。
    cond1 = s[0] == 'A'

    # S の先頭から 3 文字目と末尾から 2 文字目の間（両端含む）に大文字の C がちょうど 1 個含まれる。
    cond2 = s[2:-1].count('C') == 1

    # A, C を除く S のすべての文字は小文字である。
    cond3 = all([char.islower() for char in s if char != 'A' and char != 'C'])

    if cond1 and cond2 and cond3:
        return 'AC'

    return 'WA'

s = input()
print(actual(s))