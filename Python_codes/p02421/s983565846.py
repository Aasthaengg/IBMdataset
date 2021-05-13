n = int(input())
card = []
tc = []
hc = []

taro = 0
hanako = 0
counter = 0

i = 0
j = 0
k = 0
for i in range(n):
    card.append(list(input().split()))
    tc.append(list(card[i][0]))
    hc.append(list(card[i][1]))

    if len(card[i][0]) <= len(card[i][1]):
        counter = len(card[i][0])
    else:
        counter = len(card[i][1])
    
    for j in range(counter):
        if ord(tc[i][j].lower()) < ord(hc[i][j].lower()):
            hanako += 3
            break
        elif ord(tc[i][j].lower()) > ord(hc[i][j].lower()):
            taro += 3
            break
        else:
            if j == counter - 1:
                if len(card[i][0]) < len(card[i][1]):
                    hanako += 3
                elif len(card[i][0]) > len(card[i][1]):
                    taro += 3
                else:
                    taro += 1
                    hanako += 1

                break

print("%d %d" % (taro, hanako))
