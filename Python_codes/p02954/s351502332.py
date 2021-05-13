S = input()

n = len(S)
x = [1] * n
for i in range(n):
    if S[i] == "R" and S[i + 1] == "R":
        x[i + 2] += x[i]
        x[i] = 0

for i in reversed(range(n)):
    if S[i] == "L" and S[i - 1] == "L":
        x[i - 2] += x[i]
        x[i] = 0
            
print(*x)
