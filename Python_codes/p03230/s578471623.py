def main():
    from collections import deque
    from decimal import Decimal, getcontext

    getcontext().prec = 1000

    N = int(input())

    # {1,...,N}*2を分割
    # k個の集合があって
    # 各集合は他のk-1個の集合に対し共通要素を1個ずつ合わせてk-1個の要素をもつ

    sq = Decimal(N * 8 + 1).sqrt()
    cond = sq % 2 == 1  # 奇数か

    if not cond:
        print('No')
        return
    k = int((1 + sq) // 2)  # Decimalのままだとrangeの引数に使えない
    print('Yes')
    print(k)

    deqs = []
    it = iter(range(1, N + 1))
    for _ in range(k):
        print(k - 1, end=' ')
        t = []
        for deq in deqs:
            x = deq.popleft()
            t.append(x)
        u = []
        for _ in range(k - 1 - len(t)):
            x = next(it)
            u.append(x)
        t.extend(u)
        print(*t) # *t,*uがRE
        deqs.append(deque(u))


if __name__ == '__main__':
    main()
