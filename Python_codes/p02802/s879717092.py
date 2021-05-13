from collections import defaultdict


def mapt(fn, *args):
    return tuple(map(fn, *args))

  
def main():
    n, m = mapt(int, input().split(" "))
    # if m == 0: print(0, 0); exit()
    ac = defaultdict(int)
    pena = defaultdict(int)
    for _ in range(m):
        index, symbol = input().split(" ")
        index = int(index)
        index -= 1
        if ac[index]: continue

        if symbol == "AC": ac[index] = 1
        elif symbol == "WA": pena[index] += 1
    # print(ac, pena)
    AC = PENA = 0
    for i in range(n):
        AC += ac[i]
        if ac[i]: PENA += pena[i]
    print(AC, PENA)

main()