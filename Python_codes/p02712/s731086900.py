N = int(input())

print(sum([n + 1 for n in range(N) if (n + 1) % 3 != 0 and (n + 1) % 5 != 0]))
