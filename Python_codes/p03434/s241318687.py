n = int(input())
cards = list(map(int, input().split()))
result = 0
result2 = 0

while(cards != []):
    result += max(cards)
    cards.remove(max(cards))
    if cards != []:
        result2 += max(cards)
        cards.remove(max(cards))

print(result-result2)
