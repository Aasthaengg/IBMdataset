#?±±???(?????????)?????\???
deck = input()
#????????????(-)????±±????????\?????????????????§??????
while deck != "-":
    #?????°?????\???
    times = int(input())
    #????????????????????????
    shuffle = list(deck)
    #?????????????????????????´?
    deck_length = len(deck)
    #times????????°???????????£?????????
    for i in range(times):
        #????????§?????????????????\????????????????????§?????£?????????
        val = int(input())
        shuffle = shuffle[val:] + shuffle[:val]
    #???????????????
    print("".join(shuffle))
    #?¬?????±±????????\???
    deck = input()