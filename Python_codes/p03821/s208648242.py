N = int(input())
AB = list(reversed([list(map(int,input().split())) for _ in range(N)]))
plus = 0
for ab in AB:
    ab[0] += plus
    if ab[0]%ab[1] != 0:
        plus += ab[1]-ab[0]%ab[1]
print(plus)