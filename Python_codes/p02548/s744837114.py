N = int(input())

s = 0
m = N//2 if N%2 == 0 else N//2 + 1
for n in range(1, m):
    s += (N//n if N%n != 0 else N//n - 1)

print(s+N//2)