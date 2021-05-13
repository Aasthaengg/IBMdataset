S = list(input())
T = list(input())

count = 0

zip(S, T)

for x, y in zip(S, T):
    if x != y:
        count += 1
print(count)
