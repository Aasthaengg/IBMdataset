I = [int(input()) for _ in range(6)]

N = I[0]
M = min(I[1:])

T = -(-N // M) + 4

print(T)