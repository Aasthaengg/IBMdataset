card = [x+' '+y for x in ['S','H','C','D'] for y in [str(i) for i in range(1,14)]]
n = int(input())
for x in range(n): card.remove(input())
for x in card: print(x)

