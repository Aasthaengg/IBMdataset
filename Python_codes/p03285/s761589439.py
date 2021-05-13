def actual(N):
    oks = []

    for idx, n in enumerate(range(4, 104, 4), start=1):
        for i in range(idx + 1):
            satisfied_value = n + (3 * i)

            if satisfied_value <= 100:
                oks.append(satisfied_value)

    oks = sorted(set(oks))

    if N in oks:
        return 'Yes'

    return 'No'
  
N = int(input())
print(actual(N))