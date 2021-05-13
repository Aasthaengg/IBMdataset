# A - Prefix and Suffix

N = int(input())
s, t = [input() for i in range(2)]
delta = N

for i in range(N):
    if s[i:] == t[:N-i]:
        delta = i
        break

print(N+delta)