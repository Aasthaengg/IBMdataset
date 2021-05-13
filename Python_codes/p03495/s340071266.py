__DEUBG__ = 0


from collections import Counter

N, K = map(int, input().split())
balls = map(int, input().split())

balls = Counter(balls)
b2 = sorted(balls.items(), key=lambda item: item[1], reverse=True)

uniq_num = len(balls)

if __DEUBG__:
    print('\n'*2)
    print(len(balls))
    print(balls)
    print(b2)

if uniq_num <= K:
    print(0)
else:
    total = 0
    for i in range(uniq_num-K):
        tmp = b2.pop()
        if __DEUBG__:
            print(tmp)
        total += tmp[-1]
    print(total)