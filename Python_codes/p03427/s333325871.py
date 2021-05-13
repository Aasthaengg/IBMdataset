N = list(map(int, input()))
nines = []
total = sum(N)
nines.append(total)

for i in range(1, len(N)):
    N[-i] = 9
    N[-i-1] -= 1
    nines.append(sum(N))

print(max(nines))
