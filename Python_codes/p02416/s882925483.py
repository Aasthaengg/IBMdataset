while True:
    kazu = [int(x) for x in input()]
    if kazu == [0]:
        break
    else:
        print('{}'.format(sum(kazu)))
