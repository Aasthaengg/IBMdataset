def abc088b_card_game_for_two():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    alice = bob = 0
    for i in range(len(a)):
        if i % 2 == 0:
            alice += a.pop()
        else:
            bob += a.pop()
    print(alice - bob)
abc088b_card_game_for_two()