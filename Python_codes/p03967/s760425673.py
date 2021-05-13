

def read_input():
    s = input()
    return s

def submit():
    s = read_input()

    p_card = 0
    hands = []
    for c in s:
        if p_card == 0:
            hands.append('g')
            p_card += 1
            continue

        if c == 'p':
            if p_card > 0:
                hands.append('p')
                p_card -= 1
                continue
            else:
                hands.append('g')
                p_card += 1
                continue
        else:
            if p_card > 0:
                hands.append('p')
                p_card -= 1
                continue
            else:
                hands.append('g')
                p_card += 1
                continue

    win = 0
    loose = 0
    for a,t in zip(hands, s):
        if a == t:
            continue

        if a == 'g':
            loose += 1
        else:
            win += 1

    print(win - loose)



if __name__ == '__main__':
    submit()
