DOWN = []
EDGE = []
POOL = []

for i, c in enumerate(input()):
    if c == '\\':
        DOWN.append(i)
    elif c == '/':
        if DOWN:
            e = DOWN.pop()
            Li = i - e # Calcurate 1 line.  \______/ 
            while EDGE: # Merge connected pools.
                if EDGE[-1] > e:
                    EDGE.pop()
                    Li += POOL.pop()
                else:
                    break
            EDGE.append(e)
            POOL.append(Li)

print(sum(POOL))
print(len(POOL), *POOL)