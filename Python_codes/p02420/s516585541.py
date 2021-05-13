while True:
    cards=input()
    if cards=='-':
        break
    m=int(input())
    for i in range(m):
        sh=int(input())
        a=cards[:sh]
        b=cards[sh:]
        cards=b+a
    print(cards)
