N = int(input())
i = 0
total = 0
while True:
    total += i
    if total >= N:
        tmp = i
        break
    i += 1

for j in range(tmp, 0, -1):
    if N - tmp >= 0:
        N -= tmp
        print(tmp)
    if N == 0:
        break
    tmp -= 1
