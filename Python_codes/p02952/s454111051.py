n = int(input())

keta = len(str(n))
cnt = 0

for i in range(keta):
    if i%2 != 0: #odd
        cnt += 10**i - 10**(i-1)
    if i == keta-1 and keta%2 != 0:
        cnt += n - 10**(keta-1) + 1

print(cnt)