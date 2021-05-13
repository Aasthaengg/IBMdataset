import math
def roundup(x):
    return int(math.ceil(x/10))*10


def main():
    import math
    inlis = []
    roundlis = []
    gapdic = {}
    cnt = 0
    for i in range(5):
        a = int(input())
        inlis.append(a)
        roundlis.append(roundup(a))
        gap = roundup(a) - a
        gapdic[i] = gap
    
    gapdic= sorted(gapdic.items(), key = lambda x:x[1])
    num = 1
    ans = 0
    for tup in gapdic:
        if num != len(inlis):
            ans += roundlis[tup[0]]
            #print(tup, roundlis[tup[0]])
        else:
            ans += inlis[tup[0]]
        num += 1
    print(ans)


if __name__ == "__main__":
    main()
