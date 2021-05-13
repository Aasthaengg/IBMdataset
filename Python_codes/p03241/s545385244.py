N,M = map(int, input().split())

maxi = 1
for i in range(int(M**0.5), 0, -1):
    if M % i != 0:
        continue
    if M//i >= N:
        maxi = max(maxi, i)
    if i >= N:
        maxi = max(maxi, M//i)

print(maxi)
