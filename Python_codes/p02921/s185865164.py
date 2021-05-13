S = input()
T = input()

sm = 0

for a, b in zip(S, T):
    if a == b:
        sm += 1

print(sm)
