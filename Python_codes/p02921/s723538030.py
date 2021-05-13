S = list(input())
T = list(input())

count = 0

for i, _ in enumerate(S):
    if S[i] is T[i]:
        count += 1

print(count)
