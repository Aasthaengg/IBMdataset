def main():
    n = int(input())
    a = list(map(int, input().split()))
    plus = []
    minus = []
    for i in a:
        if i > 0:
            plus.append(i)
        elif i < 0:
            minus.append(i)
        else:
            if len(minus) == 0:
                minus.append(i)
            else:
                plus.append(i)
    plus.sort(reverse=True)
    minus.sort()
    if len(minus) == 0:
        minus.append(plus.pop())
    elif len(plus) == 0:
        plus.append(minus.pop())
    print(sum(plus)-sum(minus))
    now = minus[-1]
    for i in range(len(plus) - 1):
        print(now, plus[i])
        now -= plus[i]
    print(plus[-1], now)
    now = plus[-1] - now
    for i in range(len(minus) - 1):
        print(now, minus[i])
        now -= minus[i]
main()