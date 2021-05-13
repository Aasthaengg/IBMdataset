
def main():
    l = input().split(' ')

    s = []

    for el in l:
        if el in ["+", "-", "*"]:
            a = s.pop(-1)
            b = s.pop(-1)
            s.append(eval(str(b) + el + str(a)))
        else:
            s.append(int(el))

    print(s[0])

main()
