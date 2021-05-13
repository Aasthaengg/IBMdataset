def grading(m, f, r):
    p = m + f
    if m == -1 or f == -1: return 'F'
    if p >= 80: return 'A'
    if p >= 65: return 'B'
    if (p >= 50) or (r >= 50): return 'C'
    if p >= 30: return 'D'
    return 'F'

if __name__ == '__main__':
    while True:
        m, f, r = [int(i) for i in input().split()]
        if m == f == r == -1: break
        print(grading(m, f, r))