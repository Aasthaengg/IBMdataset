import itertools

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    l_an = [a, b, c, d, e]
    ret = "Yay!"
    for i in list(itertools.combinations(l_an, 2)):
        if i[1] - i[0] > k:
            ret = ":("
            break
    print(ret)
