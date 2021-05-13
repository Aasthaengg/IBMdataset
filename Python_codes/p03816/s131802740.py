def main():
    card_num = int(input())
    cards = list(map(int, input().split()))
    count = {}
    for card in cards:
        if card in count:
            count[card] += 1
        else:
            count[card] = 1
    answer = 0
    for c in list(count.values()):
        if c > 1:
            answer += c - 1
    if answer % 2:
        answer += 1
    print(card_num - answer)


if __name__ == '__main__':
    main()

