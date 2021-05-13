S = input()

c = 0
m = 0
acgt = ['A', 'C', 'G', 'T']
for s in S:
    if s in acgt:
        c += 1
        if c > m:
            m = c
    else:
        c = 0

print(m)