N = int(input())

if N in (1, 2):
    print(N)
    exit()

for i in range(2, 10 ** 4):
    x = i * (i + 1) / 2
    if x - (i - 1) <= N <= x:
        a = i
        break

ans = [i for i in range(1, a + 1)]
b = a*(a+1)/2 - N

for i in range(1, a+1):
    if i != b:
        print(i)

