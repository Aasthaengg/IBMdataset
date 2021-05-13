def grade(m, f, r):
    if m == -1 or f == -1:
        return 'F'
    if m + f >= 80:
        return 'A'
    if m + f >= 65:
        return 'B'
    if m + f >= 50:
        return 'C'
    if m + f >= 30:
        if r >= 50:
            return 'C'
        else:
            return 'D'
    return 'F'

while True:
    m, f, r = map(int, input().split())
    if m == -1 and f == -1 and r == -1:
        break
    print(grade(m, f, r))

