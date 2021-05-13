N = int(input())
transportations = [int(input()) for _ in range(5)]

q,r = divmod(N,min(transportations))

if r != 0:
    q += 1

output = q + 4

print(output)