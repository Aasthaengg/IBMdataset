K = int(input())

N = 50
q = K // N
r = K % N

a = (N - 1 + q) + N - (r - 1)
b = (N - 1 + q) - r

answer = [a] * r + [b] * (N - r)
print(N)
print(' '.join(list(map(str, answer))))