# ABC 119: B – Digital Gifts
N = int(input())

gift = 0

for _ in range(N):
    line = [s for s in input().split()]
    gift += float(line[0]) if line[1] == 'JPY' else 380000.0 * float(line[0])

print(gift)