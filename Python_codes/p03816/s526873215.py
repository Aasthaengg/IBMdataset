
url = "https://atcoder.jp//contests/abc057/tasks/abc057_d"

import collections

def main():
    n = int(input())
    cards = list(map(int, input().split()))
    c_cards = collections.Counter(cards)
    credit = 0
    r = 0

    for k in c_cards:
        surplus = c_cards[k] - 1
        r += surplus
        if c_cards[k] > 1:
            n -= surplus
            if credit > 0:
                credit = abs(credit - surplus%2)
            else:
                credit += surplus%2
            c_cards[k] -= surplus
    if credit > 0:
        n -= credit
    print(n)



if __name__ == '__main__':
    main()
