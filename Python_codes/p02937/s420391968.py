s = input()
t = input()
n = len(s)

alph = "abcdefghijklmnopqrstuvwxyz"
to_int = {char: i for i, char in enumerate(alph)}

set_ = set(list(s))
for char in t:
    if char not in set_:
        print(-1)
        exit()

next_ = [[0] * 26 for i in range(n + 1)]
for i in range(n)[::-1]:
    for j, char in enumerate(alph):
        if s[i] == char:
            next_[i][j] = i + 1
        else:
            next_[i][j] = next_[i + 1][j]

ans = 0
pos = 0
for char in t:
    if next_[pos][to_int[char]] == 0:
        ans += len(s)
        pos = next_[0][to_int[char]]
    else:
        pos = next_[pos][to_int[char]]
print(ans + pos)