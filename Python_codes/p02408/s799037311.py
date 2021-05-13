class Card:
    def __init__(self, s, n):
        self.suit = s
        self.num = n

class FindingMissingCards:
    def __init__(self):
        self.allCards = []
        for s in ["S","H","C","D"]:
            for n in range(1,14):
                self.allCards.append(Card(s,n))
    def find(self, cards):
        for c in cards:
            for ac in self.allCards:
                if c.num == ac.num and c.suit == ac.suit:
                    self.allCards.remove(ac)
        for c in self.allCards:
            print "%s %d" % (c.suit, c.num)

if __name__ == "__main__":
    n = int(raw_input())
    cards = []
    for i in range(n):
        s, n = raw_input().split()
        cards.append(Card(s, int(n)))

    fmc = FindingMissingCards()
    fmc.find(cards)