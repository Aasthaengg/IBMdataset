S = input()
T = input()
count = 0
for u, v in zip(S, T):
    if u != v:
        count += 1
print(count)