cards = list()
mark = ["S","H","C","D"]
for i in (mark):
    for j in range(1,14):
        cards.append( i + " " + str(j) )
n = int(input())
for i in range(n):
    a = input()
    cards.remove(a)
if len(cards) > 0:
    print("\n" .join(cards))