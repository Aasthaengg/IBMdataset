def main():
    STR = input()
    Q = int(input())
    ORDER = tuple(tuple(input().split()) for _ in range(Q))

    str_ = list(STR)
    for order in ORDER:
        s = int(order[1])
        e = int(order[2]) + 1
        a = str_[s:e]
        if order[0] == 'print':
            print(''.join(a))
        elif order[0] == 'reverse':
            a = a[::-1]
            j = s
            for i in range(s, e):
                str_[i] = a[i-j]
        elif order[0] == 'replace':
            j = s
            for i in range(s, e):
                str_[i] = order[3][i-j]

main()