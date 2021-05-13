# A - Blackjack

A = [int(a) for a in input().split()]
print('bust' if 22 <= sum(A) else 'win')
