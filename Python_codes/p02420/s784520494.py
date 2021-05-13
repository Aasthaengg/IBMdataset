while True:
    data=raw_input()
    if data=='-': break
    for _ in xrange(input()):
        index=input()
        data=data[index:]+data[:index]
    print data