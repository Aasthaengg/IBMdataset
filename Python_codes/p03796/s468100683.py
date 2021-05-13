N = int(input())
p = 1
for i in range(N):
    p = p * (i + 1) % (1e9 + 7)
print(int(p))