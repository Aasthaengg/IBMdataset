from sys import maxsize

def calc(m, f, r):
    border = [80, 65, 50, 30]
    grade = ["A", "B", "C", "D", "F"]

    if min(m, f) == -1:
        return grade[-1]
    if r >= 50:
        border[grade.index("C")] = -1 * maxsize

    i = 0
    while i < len(border) and m + f < border[i]:
        i += 1

    return grade[i]

ans = []
while True:
    m, f, r = map(int, input().split())
    if max(m, f, r) == -1:
        break
    ans.append(calc(m, f, r))

print("\n".join(ans))
