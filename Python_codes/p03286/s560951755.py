N = int(input())

S = ""
for i in range(100):
    if abs(N) % (2 ** (i+1)) != 0:
        S += "1"
        N -= (-2) ** (i)
    else:
        S += "0"
    if N == 0:
        break

print(S[::-1])