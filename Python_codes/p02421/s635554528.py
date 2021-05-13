N = input()
taro = 0
hanako = 0
for n in range(N):
    cards = raw_input().split()
    if cards[0] > cards[1]:
        taro += 3
    elif cards[0] < cards[1]:
        hanako += 3
    else:
        taro += 1
        hanako += 1
print "%d %d" % (taro, hanako)