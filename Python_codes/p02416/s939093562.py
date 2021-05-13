while True:
    inp = input()
    if inp == "0": break
    s = 0
    print(sum(list(map(int,list(inp)))))