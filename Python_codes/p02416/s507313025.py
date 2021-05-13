while True:
    a=str(raw_input())
    if a=="0": break
    print(sum([int(i) for i in a]))