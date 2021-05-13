def area(higt, wide):
    a = higt
    b = wide
    return a * b

def circ(higt, wide):
    a = higt
    b = wide
    return 2 * int(a) + 2 * int(b)


imput = raw_input().split()
menseki = area(int(imput[0]), int(imput[1]))
ensyu = circ(imput[0], imput[1])

print(str(menseki) + " " + str(ensyu))