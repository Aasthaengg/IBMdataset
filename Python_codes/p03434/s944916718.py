N = int(input())
Card = list(map(int,input().split()))

Card.sort(reverse=True)

if len(Card)>=2:
    A = sum(Card[::2])
    B = sum(Card[1::2])
else:
    A = Card[0]
    B = 0

print(A-B)