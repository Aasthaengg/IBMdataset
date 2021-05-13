card=[]
while True:
    s=raw_input()
    if s=="-":
        break
    for i in s:
        card.append(i)
    shuffle=input()
    for i in xrange(shuffle):
        h=input()
        card+=card[0:h]
        del card[0:h]
    print("".join(card))
    del card[0:len(card)]