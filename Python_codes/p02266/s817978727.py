s = raw_input()

St1, St2 = [], []
sumv = 0

for i in range(len(s)):
    if s[i] == '\\':
        St1.append(i)
    elif s[i] == '/' and len(St1) > 0:
        j = St1.pop()
        a = i-j
        sumv += a
        while len(St2) > 0 and St2[-1][0] > j:
            a += St2.pop()[1]

        St2.append([j, a])

St2.insert(0, [0, len(St2)])

print sumv
print ' '.join(map(lambda x: str(x[1]), St2))