s = input()
N = len(s)
s_trim = ''.join([c for c in s if c != 'x'])
N_trim = len(s_trim)

def check_anagram():
    for i in range(N_trim):
        j = N_trim - 1 - i
        if s_trim[i] != s_trim[j]:
            return False
    return True

def solve():
    if not check_anagram():
        return -1
    if N_trim == 0:
        return 0
    # Center of anagram
    pr = N_trim // 2
    pl = pr
    if N_trim % 2 == 0:
        pl -= 1

    xl = 0
    tl = 0
    while xl < N:
        if s[xl] != 'x':
            # assert s[xl] == s_trim[tl]
            if tl == pl:
                break
            tl += 1
        xl += 1

    if N_trim % 2 == 1:
        xr = xl
    else:
        xr = xl + 1
        while s[xr] == 'x':
            xr += 1

    cost = 0
    while True:
        # assert s[xl] == s_trim[pl]
        # assert s[xr] == s_trim[pr]
        # assert s[xl] == s[xr]
        # assert s_trim[pl] == s_trim[pr]
        pl -= 1; pr += 1
        while True:
            xl -= 1; xr += 1
            if not (xl >= 0 and xr < N and s[xl] == 'x' and s[xr] == 'x'):
                break
        while xl >= 0 and s[xl] == 'x':
            cost += 1
            xl -= 1
        while xr < N and s[xr] == 'x':
            cost += 1
            xr += 1
        if pl < 0 and pr >= N_trim and xl < 0 and xr >= N:
            return cost

print(solve())
