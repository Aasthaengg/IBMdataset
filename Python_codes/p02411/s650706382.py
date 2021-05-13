def seiseki(m, f, r):
    if m == -1 or f == -1:
        return 'F'
    else:
        t = m + f
    
        if t >= 80:
            return 'A'
        elif 65 <= t < 80:
            return 'B'
        elif 50 <= t < 65:
            return 'C'
        elif 30 <= t < 50:
            if r >= 50:
                return 'C'
            else:
                return 'D'
        else:
            return 'F'

res = []
while True:
    m, f, v = map(int, input().split())
    if m == f == v == -1:
        break;
    res.append(seiseki(m, f, v))

for i in range(len(res)):
    print(res[i])