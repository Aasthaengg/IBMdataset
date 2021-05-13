score = []
while True:
    m, f, r = map(int, input().strip().split())
    if m == f == r == -1:
        break
    elif m == -1 or f == -1 or m + f < 30:
        score.append('F')
    elif m + f < 50 and r < 50:
        score.append('D')
    elif m + f < 65:
        score.append('C')
    elif m + f < 80:
        score.append('B')
    else:
        score.append('A')

print('\n'.join(score))