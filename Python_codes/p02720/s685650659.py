K = int(input())
ls = []
def rec(digit, ini):
    ls.append(ini)
    if digit == 10: #最大10けたなので(sample4)
        return
    deltas = []
    if ini % 10 == 0:
        deltas = [0, 1]
    elif ini % 10 == 9:
        deltas = [-1, 0]
    else:
        deltas = [-1, 0, 1]
    for delta in deltas:
        new = ini * 10 + ini % 10 + delta
        rec(digit+1, new)

for ini in range(1, 10):
    rec(1, ini)
print(sorted(ls)[K-1])